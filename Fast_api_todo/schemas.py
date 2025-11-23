from pydantic import BaseModel

class Todobase(BaseModel):
    title:str
    description:str|None=None
    completed:bool=False

class TodoCreate(Todobase):
    pass

class Todo(Todobase):
    id:int
    class config:
        orm_mode=True