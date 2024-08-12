from pydantic import BaseModel, ConfigDict


class StudentBase(BaseModel):
    first_name: str
    last_name: str
    year: int


class Student(StudentBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class StudentCreate(StudentBase):
    pass
