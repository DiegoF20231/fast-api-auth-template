from dataclasses import dataclass
from datetime import datetime, timezone
from pydantic import BaseModel
from typing import Generic, TypeVar

from src.modules.common.classes.error import Error

TBody = TypeVar('TBody')


class ApiResponse(BaseModel, Generic[TBody],):
    timestamp: str
    body: TBody
    message: str

    @staticmethod
    def create(body: TBody, message: str):
        return ApiResponse(
            timestamp=str(datetime.now(timezone.utc)),
            body=body,
            message=message).model_dump()
