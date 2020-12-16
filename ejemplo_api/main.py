from db.item_db import ItemInDB
from db.item_db import update_item, get_item

from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()

@app.get("/items/{item_id}")
async def item_get(item_id: int): 
    item_in = get_item(item_id)
    if item_in == None: 
        raise HTTPException(status_code=400,
            detail="El item no fue encontrado")
@app.put("/producto/{item_id}")
async def (item_id: int, item: ItemIn): 
    item_in = get_item(item_id)

    if item_in == None: 
        raise HTTPException(status_code=400,
            detail="El item no existe")
    