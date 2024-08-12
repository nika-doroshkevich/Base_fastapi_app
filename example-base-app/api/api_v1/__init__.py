from fastapi import (
    APIRouter,
    Depends,
)
from fastapi.security import HTTPBearer

from core.config import settings
from .auth import router as auth_router
from .messages import router as messages_router
from .quartal_grades import router as quartal_grades_router
from .student_grades import router as student_grades_router
from .students import router as students_router
from .users import router as users_router

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix=settings.api.v1.prefix,
    dependencies=[Depends(http_bearer)],
)
router.include_router(auth_router)
router.include_router(users_router)
router.include_router(messages_router)
router.include_router(students_router)
router.include_router(student_grades_router)
router.include_router(quartal_grades_router)
