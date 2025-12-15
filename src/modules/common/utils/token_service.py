import jwt

from src.modules.common.utils.jwt_settings import jwt_settings

SECRET_KEY = "SUPER_SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 9000


class TokenService:

    @staticmethod
    def generate_token(data: dict) -> str:
        token = jwt.encode(
            payload=data, key=jwt_settings.jwt_secret, algorithm=jwt_settings.jwt_algorithm,)
        return token

    @staticmethod
    def decode_token(token: str) -> dict:
        decoded_data = jwt.decode(
            jwt=token, key=jwt_settings.jwt_secret, algorithms=[jwt_settings.jwt_algorithm],)

        return decoded_data
