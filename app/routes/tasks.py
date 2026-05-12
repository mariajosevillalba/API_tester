from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import TaskDB, UserDB
from ..schemas import Task

router = APIRouter()

@router.post("/tasks", status_code=201)
def create_task(task: Task):

    db: Session = SessionLocal()

    user = db.query(UserDB).filter(
        UserDB.id == task.user_id
    ).first()

    if not user:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Usuario no existe"
        )

    new_task = TaskDB(**task.dict())

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    db.close()

    return new_task


@router.get("/tasks")
def get_tasks():

    db = SessionLocal()

    tasks = db.query(TaskDB).all()

    db.close()

    return tasks


@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):

    db = SessionLocal()

    task = db.query(TaskDB).filter(
        TaskDB.id == task_id
    ).first()

    if not task:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    db.delete(task)
    db.commit()

    db.close()

    return