from sqlalchemy.orm import Session
from fastapi import HTTPException
import random
from models.training import Training
from models.answer import Answer



def create_training(db: Session, user_id: int, category: str, length: int):
    if not category in ['numbers', 'binary']:
        raise HTTPException(status_code=404, detail="category not found")

    sequence = getSequence(category, length)

    training = Training(
        user_id=user_id, 
        category=category, 
        length=length, 
        sequence=sequence,
    )
    
    db.add(training)
    db.commit()
    db.refresh(training)
    return training


def get_training(db: Session, id: int):
    training = db.query(Training).filter(Training.id == id).first()

    if not training:
        raise HTTPException(status_code=404, detail="training not found")
    
    return training



def getSequence(category: str, length: int):
    num = ""
    if category == 'numbers':
        for i in range(length):
            num += str(random.randint(0, 9))
    elif category == 'binary':
        for i in range(length):
            num += str(random.randint(0, 1))
    return num


def answer(db: Session, id: int, provided: str):
    training = db.query(Training).filter(Training.id==id).first()

    if not training:
        raise HTTPException(status_code=404, detail="training not found")
    
    answer = Answer(
        training_id = id,
        expected = training.sequence,
        provided = provided,
        correct = (provided == training.sequence)
    )
    db.add(answer)
    db.commit()
    db.refresh(answer)
    return answer