from typing import Dict
from pydantic import BaseModel 

class ItemInDB(BaseModel): 
    id: int 
    name: str 
    price: float 

database_items = Dict[int, ItemInDB]

database_items = {
    100:ItemInDB(**{"id":100,
        "name":"Galletas",
        "price":350.6,
        }),
    101:ItemInDB(**{"id":101,
        "name":"Pan",
        "price":106.6,
})
}

def get_item(llave: int): 
    if llave in database_items.keys(): 
        return 