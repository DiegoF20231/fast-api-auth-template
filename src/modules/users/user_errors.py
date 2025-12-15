from ..common.classes.error import Error


class UserErrors:
    USER_NOT_FOUND: Error = Error(
        code="USER_NOT_FOUND", description="The specified user does not exist.")

    INVALID_CREDENTIALS = Error(
        code="INVALID_CREDENTIALS", description="The provided credentials are invalid.")

    USER_WITH_EMAIL_ALREADY_EXISTS = Error(
        code="USER_WITH_EMAIL_ALREADY_EXISTS", description="A user with the given email already exists.")

    UNAUTHORIZED_ACCESS = Error(
        code="UNAUTHORIZED_ACCESS", description="You do not have permission to access this resource.")
