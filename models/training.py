from core.database import Base
from sqlalchemy import Column, String, Integer
from pydantic import BaseModel, ConfigDict


class Training(Base):
    __tablename__ = "trainings"

    id = Column(Integer(), primary_key=True, index=True)
    user_id = Column(Integer(), nullable=True)
    category = Column(String(31), nullable=False)
    length = Column(Integer(), nullable=False)
    sequence = Column(String(1000))


class CreateTraining(BaseModel):
    user_id: int
    category: str
    length: int

class ResponseTraining(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    category: str
    length: int
    sequence: str
