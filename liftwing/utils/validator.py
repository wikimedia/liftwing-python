from functools import wraps
from pydantic import BaseModel


def validate_payload(model: BaseModel):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            payload = kwargs.get('payload', None)
            if payload is None:
                raise ValueError("Missing 'payload' in arguments")

            _ = model(**payload)

            return func(*args, **kwargs)
        return wrapper
    return decorator
