from sqlalchemy.ext.asyncio import AsyncSession

from core.models import QuartalGrade
from core.schemas.quartal_grade import QuartalGradeCreate


async def create_quartal_grade(
        session: AsyncSession, quartal_grade: QuartalGradeCreate
) -> QuartalGrade:
    quartal_grade = QuartalGrade(**quartal_grade.model_dump())
    session.add(quartal_grade)
    await session.commit()
    return quartal_grade
