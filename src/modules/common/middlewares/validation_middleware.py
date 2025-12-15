from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI, status

from src.modules.common.classes.api_response import ApiResponse
from src.modules.common.classes.error import ValidationErrorDetail


def register_validation_exception_handler(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        # errors = [{"field": err['loc'][1], "message": err['msg']}
        #           for err in exc.errors()]
        errors = [ValidationErrorDetail(
            property=".".join(str(x) for x in err["loc"] if x != "body"), error=err['msg'], type=err['type']) for err in exc.errors()]
        return JSONResponse(
            status_code=422,
            content=ApiResponse.create(
                body=errors,
                message="Validation Error"
            )
        )
