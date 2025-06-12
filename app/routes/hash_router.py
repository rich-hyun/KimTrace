from fastapi import APIRouter
from pydantic import BaseModel
import hashlib

router = APIRouter()

class HashInput(BaseModel):
    model: str
    output: list

@router.post("/hash")
async def generate_hash(payload: HashInput):
    data_str = payload.model + str(payload.output)
    hash_value = hashlib.sha256(data_str.encode()).hexdigest()
    return {"hash": hash_value}
