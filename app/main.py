from fastapi import FastAPI
from app.routes import hash_router
from app.routes import send_router


app = FastAPI()

app.include_router(hash_router.router)
app.include_router(send_router.router)