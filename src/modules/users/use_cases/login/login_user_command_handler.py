from src.modules.common.abstractions.handler import RequestHandler
from src.modules.common.classes.result import Result
from src.modules.common.utils.password_hasher import PasswordHasher
from src.modules.common.utils.token_service import TokenService
from src.modules.users.use_cases.login.login_user_response import LoginUserResponse
from src.modules.users.user import User
from src.modules.users.user_errors import UserErrors
from ..login.login_user_command import LoginUserCommand
from dataclasses import dataclass


@dataclass
class LoginUserCommandHandler(RequestHandler):

    def handle(self, command: LoginUserCommand) -> Result:
        existing_user = self.db.query(User).filter_by(
            email=command.email).first()

        if not existing_user:
            return Result.failure(UserErrors.INVALID_CREDENTIALS)
        match = PasswordHasher.verify_password(
            command.password, existing_user.password)

        if not match:
            return Result.failure(UserErrors.INVALID_CREDENTIALS)

        token = TokenService.generate_token(
            data={"user_id": existing_user.user_id, "email": existing_user.email})

        response = LoginUserResponse(token=token)

        return Result.success(response)
