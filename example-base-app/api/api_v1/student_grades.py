from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper
from core.schemas.student_grade import StudentGrade, StudentGradeCreate
from crud import student_grades

router = APIRouter(
    prefix=settings.api.v1.student_grades,
    tags=["StudentGrade"],
)


@router.post(
    "/",
    response_model=StudentGrade,
    status_code=status.HTTP_201_CREATED,
)
async def create_student_grade(
        student_grade: StudentGradeCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    return await student_grades.create_student_grade(session=session, student_grade=student_grade)
