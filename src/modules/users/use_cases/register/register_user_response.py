from dataclasses import dataclass
from pydantic import BaseModel
from src.modules.users.user import User


class RegisterUserResponse(BaseModel):
    user_id: str
    username: str
    email: str
