from fastapi import FastAPI
from todo import models
from todo.database import engine
from todo.routers import todo, user, authentication

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(todo.router)
app.include_router(user.router)
app.include_router(authentication.router)

