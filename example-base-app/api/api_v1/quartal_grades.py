from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper
from core.schemas.quartal_grade import QuartalGrade, QuartalGradeCreate
from crud import quartal_grades

router = APIRouter(
    prefix=settings.api.v1.quartal_grades,
    tags=["QuartalGrade"],
)


@router.post(
    "/",
    response_model=QuartalGrade,
    status_code=status.HTTP_201_CREATED,
)
async def create_quartal_grade(
        quartal_grade: QuartalGradeCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    return await quartal_grades.create_quartal_grade(session=session, quartal_grade=quartal_grade)
