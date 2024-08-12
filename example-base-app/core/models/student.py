from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin

if TYPE_CHECKING:
    from .quartal_grade import QuartalGrade
    from .student_grade import StudentGrade


class Student(Base, IntIdPkMixin):
    first_name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(40))
    year: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.utcnow,
    )

    student_grades: Mapped[list["StudentGrade"]] = relationship(back_populates="student")
    quartal_grades: Mapped[list["QuartalGrade"]] = relationship(back_populates="student")
