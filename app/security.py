from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader

# API key configuration
API_KEYS = ["your_api_key_1", "your_api_key_2"]  # Add your valid API keys here
API_KEY_REQUIRED = True  # Set to False to allow access without API keys

# FastAPI security dependency
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


async def verify_api_key(api_key: str = Depends(api_key_header)):
    """
    Verify the API key from the request header.

    Args:
        api_key: API key from X-API-Key header

    Raises:
        HTTPException: If API key is required but missing or invalid
    """
    if API_KEY_REQUIRED:
        if not api_key or api_key not in API_KEYS:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid or missing API key"
            )
    return api_key
