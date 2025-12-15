from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt

from src.modules.common.classes.api_response import ApiResponse
from src.modules.common.utils.token_service import TokenService
from src.modules.users.user_errors import UserErrors

security = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    try:
        token = credentials.credentials
        payload = TokenService.decode_token(token)
    except jwt.InvalidTokenError as e:
        print(e)
        raise HTTPException(status_code=401, detail=ApiResponse.create(
            body=UserErrors.UNAUTHORIZED_ACCESS, message="Invalid token"))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail=ApiResponse.create(
            body=None, message="Could not validate credentials"))
    return payload
