from scalar_fastapi import Theme, get_scalar_api_reference
from src.modules.database.database import init_db
from src.modules.users.user_routes import auth_router
from fastapi import FastAPI
from src.modules.users.user_errors import UserErrors
from src.modules.common.middlewares.validation_middleware import register_validation_exception_handler

app = FastAPI(title="Auth Template API", version="1.0.0", openapi_tags=[{
    "name": "Auth",
    "description": "Authentication related endpoints"
}])

init_db()

app.include_router(auth_router)
register_validation_exception_handler(app)


@app.get("/scalar", include_in_schema=False)
def scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Template Auth API Scalar Reference",
        theme=Theme.KEPLER

    )
