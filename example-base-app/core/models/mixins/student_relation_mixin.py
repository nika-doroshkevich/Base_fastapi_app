from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from core.models.student import Student


class StudentRelationMixin:
    _student_id_nullable: bool = False
    _student_id_unique: bool = False
    _student_back_populates: str | None = None

    @declared_attr
    def student_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("students.id"),
            unique=cls._student_id_unique,
            nullable=cls._student_id_nullable,
        )

    @declared_attr
    def student(cls) -> Mapped["Student"]:
        return relationship(
            "Student",
            back_populates=cls._student_back_populates,
        )
