from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.training import ResponseTraining, CreateTraining
from models.answer import ResponseAnswer, CreateAnswer
from services import memory_services
from core.database import get_db

router = APIRouter(prefix="/training",tags=["Training"])

@router.get("/{id}", response_model=ResponseTraining)
def get_training(id: int, db: Session = Depends(get_db)):
    return memory_services.get_training(db, id=id)

@router.post("/", response_model=ResponseTraining)
def create_training(training: CreateTraining, db: Session = Depends(get_db)):
    return memory_services.create_training(
        db=db,
        user_id=training.user_id,
        category=training.category,
        length=training.length
    )

@router.post("/{id}/answer", response_model=ResponseAnswer)
def answer(id: int, answer: CreateAnswer, db: Session = Depends(get_db)):
    return memory_services.answer(db, id=id, provided=answer.provided)