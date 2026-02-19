from core.database import Base
from sqlalchemy import Column, String, ForeignKey, Boolean, Integer
from sqlalchemy.orm import mapped_column
from pydantic import BaseModel


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer(), primary_key=True, index=True)
    training_id = mapped_column(ForeignKey("trainings.id"))
    expected = Column(String())
    provided = Column(String())
    correct = Column(Boolean())


class CreateAnswer(BaseModel):
    provided: str

class ResponseAnswer(BaseModel):
    training_id: int
    expected: str
    provided: str
    correct: bool