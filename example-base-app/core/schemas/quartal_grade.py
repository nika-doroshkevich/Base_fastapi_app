from pydantic import BaseModel, ConfigDict


class QuartalGradeBase(BaseModel):
    quartal: str
    subject: str
    grade: int
    student_id: int


class QuartalGrade(QuartalGradeBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class QuartalGradeCreate(QuartalGradeBase):
    pass
