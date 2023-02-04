from pydantic import BaseModel
from typing import List
from typing import Union

class Todo(BaseModel):
    title : str
    desc : str
    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    todo_table : List[Todo] = []
    class Config:
        orm_mode = True 


class ShowUserWithoutPass(BaseModel):
    name: str
    email: str
    class Config:
        orm_mode = True 


class ShowTodo(BaseModel):
    title : str
    desc : str
    creator : ShowUserWithoutPass
    class Config():
        orm_mode = True  


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None