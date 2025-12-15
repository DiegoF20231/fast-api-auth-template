from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from src.modules.common.classes.api_response import ApiResponse
from src.modules.common.classes.error import Error, ValidationErrorDetail
from src.modules.database.database import get_db
from src.modules.users.security import get_current_user
from src.modules.users.use_cases.login.login_user_command import LoginUserCommand
from src.modules.users.use_cases.login.login_user_command_handler import LoginUserCommandHandler
from sqlalchemy.orm import Session
from src.modules.users.use_cases.login.login_user_response import LoginUserResponse
from src.modules.users.use_cases.register.register_user_command import RegisterUserCommand
from src.modules.users.use_cases.register.register_user_command_handler import RegisterUserCommandHandler
from fastapi import status
from src.modules.common.classes.api_response import ApiResponse
from src.modules.users.use_cases.register.register_user_response import RegisterUserResponse


auth_router = APIRouter(
    prefix="/api/auth",
    tags=["Auth"],)


@auth_router.post("/register",
                  status_code=201,
                  description="Register a new user",
                  name="Register User",
                  summary="User Registration",
                  response_description="Details of the newly registered user",
                  responses={
                      201: {
                          "model": ApiResponse[RegisterUserResponse],
                          "description": "User registered successfully"
                      },
                      400: {
                          "model": ApiResponse[Error],
                          "description": "Registration failed"
                      }
                  }

                  )
def register_user(command: RegisterUserCommand, db: Session = Depends(get_db)):
    result = RegisterUserCommandHandler(db=db).handle(command)
    print(result)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=ApiResponse.create(body=result.value, message="User registered")) if result.is_success else JSONResponse(status_code=400, content=ApiResponse.create(body=result.error, message="Registration failed"))


@auth_router.post("/login",
                  description="Login a user and return an authentication token",
                  name="Login User",
                  summary="User Login",
                  response_description="Authentication token up on successful login",
                  responses={
                      200: {
                          "model": ApiResponse[LoginUserResponse],
                          "description": "Login successful"
                      },
                      400: {
                          "model": ApiResponse[Error],
                          "description": "Login faileasasad"
                      },
                      422: {
                          "model": ApiResponse[ValidationErrorDetail],
                          "description": "Validation Error"
                      }
                  })
def login_user(command: LoginUserCommand, db: Session = Depends(get_db)):
    result = LoginUserCommandHandler(db=db).handle(command)
    return JSONResponse(status_code=200, content=ApiResponse.create(body=result.value, message="Login")) if result.is_success else JSONResponse(status_code=400, content=ApiResponse.create(body=result.error, message="Login failed"))


@auth_router.get("/profile")
def get_user_profile(current_user=Depends(get_current_user)):

    return JSONResponse(status_code=200, content={"message": "User profile endpoint", "user": current_user})
