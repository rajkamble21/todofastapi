from sqlalchemy import Column, Integer, String, ForeignKey
from todo.database import Base
from sqlalchemy.orm import relationship

class Todo(Base):
    __tablename__ = "todo_table"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(25))
    desc = Column(String(100))
    user_id = Column(Integer, ForeignKey('user_table.id'))
    creator = relationship("User", back_populates="todo_table")

class User(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))
    todo_table = relationship("Todo", back_populates="creator")
