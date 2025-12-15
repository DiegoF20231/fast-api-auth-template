from dataclasses import asdict, dataclass
from sqlalchemy.orm import Session
from src.modules.common.classes.result import Result
from src.modules.common.abstractions.handler import RequestHandler
from src.modules.common.utils.password_hasher import PasswordHasher
from src.modules.users.use_cases.register.register_user_command import RegisterUserCommand
from src.modules.users.use_cases.register.register_user_response import RegisterUserResponse
from src.modules.users.user import User
from src.modules.users.user_errors import UserErrors
import uuid


@dataclass
class RegisterUserCommandHandler(RequestHandler):

    def handle(self, command: RegisterUserCommand) -> Result:
        existing_user = self.db.query(User).filter_by(
            email=command.email).first()
        if existing_user:
            return Result.failure(UserErrors.USER_WITH_EMAIL_ALREADY_EXISTS)

        hashed_password = PasswordHasher.hash_password(command.password)
        new_user = User(
            user_id=str(uuid.uuid4()),
            username=command.username,
            email=command.email,
            password=hashed_password

        )

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        response = RegisterUserResponse(
            user_id=new_user.user_id,
            username=new_user.username,
            email=new_user.email
        )

        return Result.success(response)
