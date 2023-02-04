from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from todo import models, schemas


def get_all(db: Session):
    todos = db.query(models.Todo).all()
    return todos


def create(request: schemas.Todo, db: Session):
    new_todo = models.Todo(title = request.title, desc = request.desc, user_id = 1)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def destroy(id:int, db: Session):
    todo = db.query(models.Todo).filter(models.Todo.id == id)
    if not todo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with that id {id} not found")
    todo.delete(synchronize_session=False)
    db.commit()


def update(id:int, request: schemas.Todo, db:Session):
    todo = db.query(models.Todo).filter(models.Todo.id == id)
    if not todo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with that id {id} not found")
    todo.update(request.dict())
    db.commit()


def show(id:int, db:Session):
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with that id {id} not found")
    return todo