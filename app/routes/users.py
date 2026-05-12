from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import UserDB
from ..schemas import User

router = APIRouter()

@router.post("/users", status_code=201)
def create_user(user: User):

    db: Session = SessionLocal()

    existing_user = db.query(UserDB).filter(
        UserDB.email == user.email
    ).first()

    if existing_user:
        db.close()
        raise HTTPException(
            status_code=409,
            detail="Email ya existe"
        )

    new_user = UserDB(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    db.close()

    return new_user


@router.get("/users")
def get_users():

    db = SessionLocal()

    users = db.query(UserDB).all()

    db.close()

    return users


@router.get("/users/{user_id}")
def get_user(user_id: int):

    db = SessionLocal()

    user = db.query(UserDB).filter(
        UserDB.id == user_id
    ).first()

    db.close()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return user


@router.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):

    db = SessionLocal()

    user = db.query(UserDB).filter(
        UserDB.id == user_id
    ).first()

    if not user:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    user.name = updated_user.name
    user.email = updated_user.email

    db.commit()
    db.refresh(user)

    db.close()

    return user


@router.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):

    db = SessionLocal()

    user = db.query(UserDB).filter(
        UserDB.id == user_id
    ).first()

    if not user:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    db.delete(user)
    db.commit()

    db.close()

    return