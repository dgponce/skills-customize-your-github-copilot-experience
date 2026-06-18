from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"id": item_id, "name": f"Item {item_id}"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("starter_code:app", host="127.0.0.1", port=8000, reload=True)
