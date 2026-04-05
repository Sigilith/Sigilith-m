from starlette.middleware.base import BaseHTTPMiddleware
class SecurityMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # Your middleware logic here
        response = await call_next(request)
        return response
