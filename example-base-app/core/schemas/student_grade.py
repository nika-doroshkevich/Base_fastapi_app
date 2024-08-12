from pydantic import BaseModel, ConfigDict


class StudentGradeBase(BaseModel):
    subject: str
    grade: int
    student_id: int


class StudentGrade(StudentGradeBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class StudentGradeCreate(StudentGradeBase):
    pass
