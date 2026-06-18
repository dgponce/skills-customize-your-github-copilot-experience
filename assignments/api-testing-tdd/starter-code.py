from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = ""
    price: float

_db: Dict[int, Item] = {}
_next_id = 1

@app.post('/items/', status_code=201)
def create_item(item: Item):
    global _next_id
    item_id = _next_id
    _db[item_id] = item
    _next_id += 1
    return {"id": item_id, **item.dict()}

@app.get('/items/')
def list_items():
    return [{"id": i, **it.dict()} for i, it in _db.items()]

@app.get('/items/{item_id}')
def get_item(item_id: int):
    item = _db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')
    return {"id": item_id, **item.dict()}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    if item_id not in _db:
        raise HTTPException(status_code=404, detail='Item not found')
    _db[item_id] = item
    return {"id": item_id, **item.dict()}

@app.delete('/items/{item_id}', status_code=204)
def delete_item(item_id: int):
    if item_id not in _db:
        raise HTTPException(status_code=404, detail='Item not found')
    del _db[item_id]
    return {}
