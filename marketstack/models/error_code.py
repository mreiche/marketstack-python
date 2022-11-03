from enum import Enum


class ErrorCode(str, Enum):
    INVALID_ACCESS_KEY = "invalid_access_key"
    MISSING_ACCESS_KEY = "missing_access_key"
    FUNCTION_ACCESS_RESTRICTED = "function_access_restricted"
    INACTIVE_USER = "inactive_user"
    HTTPS_ACCESS_RESTRICTED = "https_access_restricted"
    INVALID_API_FUNCTION = "invalid_api_function"
    NOT_FOUND = "404_not_found"
    USAGE_LIMIT_REACHED = "usage_limit_reached"
    RATE_LIMIT_REACHED = "rate_limit_reached"
    INTERNAL_ERROR = "internal_error"
    VALIDATION_ERROR = "validation_error"

    def __str__(self) -> str:
        return str(self.value)
