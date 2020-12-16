from fastapi import Depends, FastAPI

from routers.user_router import router as router_users  
from routers.transaction_router import router as router_transactions

api = FastAPI()

api.include_router(router_users)
api.include_router(router_transactions)
