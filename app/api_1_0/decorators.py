from functools import wraps
from flask import abort, g
from flask_login import current_user
from .errors import forbidden
from ..models import Permission


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('Insufficient permissions 没有足够的权限.')
            return f(*args, **kwargs)
        return decorated_function
    return decorator
