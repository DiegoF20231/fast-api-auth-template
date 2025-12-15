
from pydantic import BaseModel, EmailStr, Field


class LoginUserCommand(BaseModel):
    """Command to log in a user."""
    email: EmailStr = Field(..., description="The user's email address", examples=[
        "jhon@gmail.com", "jane@gmail.com"])
    password: str = Field(..., min_length=6, description="The user's password", examples=[
        "password123", "password456"])
