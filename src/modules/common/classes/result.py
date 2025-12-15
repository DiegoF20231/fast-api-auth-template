from dataclasses import dataclass
from .error import Error


@dataclass
class Result:
    is_success: bool
    error: Error
    value: any = None

    @staticmethod
    def success(value: any = None) -> Result:
        return Result(is_success=True, error=None, value=value)

    @staticmethod
    def failure(error: Error) -> Result:
        return Result(is_success=False, error=error)
