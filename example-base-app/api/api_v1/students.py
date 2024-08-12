from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper
from core.schemas.student import Student, StudentCreate
from crud import students

router = APIRouter(
    prefix=settings.api.v1.students,
    tags=["Students"],
)


@router.post(
    "/",
    response_model=Student,
    status_code=status.HTTP_201_CREATED,
)
async def create_student(
        student: StudentCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    return await students.create_student(session=session, student=student)
