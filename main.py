from typing import Union
from fastapi import FastAPI
"""
Receives HTTP requests in the paths / and /items/{item_id}.
Both paths take GET operations (also known as HTTP methods).
The path /items/{item_id} has a path parameter item_id that should be an int.
The path /items/{item_id} has an optional str query parameter q.
"""

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str,None] = None):
    return {"item_id":item_id,"q":q}