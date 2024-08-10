from fastapi_users import FastAPIUsers

from core.models import User
from core.types.user_id import UserIdType

from .backend import authentication_backend
from .user_manager import get_user_manager

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)
