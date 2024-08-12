from sqlalchemy.ext.asyncio import AsyncSession

from core.models import StudentGrade
from core.schemas.student_grade import StudentGradeCreate


async def create_student_grade(
        session: AsyncSession, student_grade: StudentGradeCreate
) -> StudentGrade:
    student_grade = StudentGrade(**student_grade.model_dump())
    session.add(student_grade)
    await session.commit()
    return student_grade
