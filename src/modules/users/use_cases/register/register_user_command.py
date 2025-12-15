from pydantic import BaseModel, Field, EmailStr


class RegisterUserCommand(BaseModel):
    """Command to register a new user."""
    username: str = Field(..., min_length=3,
                          max_length=50,
                          description="The user's username", examples=["john_doe", "jane_smith"])
    email: EmailStr = Field(..., description="The user's email address", examples=[
                            "jhon@gmail.com", "jane@gmail.com"])
    password: str = Field(..., min_length=6, description="The user's password", examples=[
                          "password123", "password456"])
