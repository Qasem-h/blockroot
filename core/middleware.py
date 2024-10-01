from starlette.middleware.base import BaseHTTPMiddleware
from loguru import logger
import time

class RequestLoggerMiddleware(BaseHTTPMiddleware):
    """Middleware to log request processing times."""

    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        logger.info(f"{request.method} {request.url} completed in {process_time:.4f}s")
        return response
