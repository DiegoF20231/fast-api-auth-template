from pydantic import BaseModel


class Error(BaseModel):
    code: str
    description: str


class ValidationErrorDetail(BaseModel):
    property: str
    error: str
    type: str
