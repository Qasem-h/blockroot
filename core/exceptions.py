from fastapi import HTTPException

class ResourceNotFoundException(HTTPException):
    def __init__(self, detail: str = "Resource not found"):
        super().__init__(status_code=404, detail=detail)

class InvalidCredentialsException(HTTPException):
    def __init__(self, detail: str = "Invalid credentials"):
        super().__init__(status_code=401, detail=detail)

class UnauthorizedAccessException(HTTPException):
    def __init__(self, detail: str = "Unauthorized access"):
        super().__init__(status_code=403, detail=detail)
