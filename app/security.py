from flask import request, abort

API_KEYS = ["your_api_key_1", "your_api_key_2"]  # Add your valid API keys here
API_KEY_REQUIRED = True  # Set to False to allow access without API keys

def api_key_auth_middleware(func):
    def wrapper(*args, **kwargs):
        if API_KEY_REQUIRED:
            api_key = request.headers.get('X-API-Key')
            if api_key not in API_KEYS:
                abort(403)  # Forbidden
        return func(*args, **kwargs)
    return wrapper
