from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Student
from core.schemas.student import StudentCreate


async def create_student(session: AsyncSession, student: StudentCreate) -> Student:
    student = Student(**student.model_dump())
    session.add(student)
    await session.commit()
    return student
