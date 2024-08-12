from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin
from .mixins.student_relation_mixin import StudentRelationMixin


class StudentGrade(Base, IntIdPkMixin, StudentRelationMixin):
    _student_back_populates = "student_grades"

    subject: Mapped[str] = mapped_column(String(40))
    grade: Mapped[int]
