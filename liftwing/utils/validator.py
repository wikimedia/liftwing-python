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


def check_required_fields(values: dict, required_fields: list):
    for field_name in required_fields:
        if field_name not in values or not values[field_name]:
            raise ValueError(f"'{field_name}' parameter is required in the payload.")
    return values
