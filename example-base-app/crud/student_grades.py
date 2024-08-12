from sqlalchemy import func
from sqlalchemy import select
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


async def get_students_with_min_grade(session: AsyncSession) -> list[StudentGrade]:
    stmt = select(func.min(StudentGrade.grade))
    result = await session.execute(stmt)
    min_grade = result.scalar_one()

    stmt_min = select(StudentGrade).where(StudentGrade.grade == min_grade)
    students_min = await session.scalars(stmt_min)

    return list(students_min)
