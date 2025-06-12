from fastapi import APIRouter
from pydantic import BaseModel
import hashlib
from app.services.blockchain_service import contract


router = APIRouter()

class HashInput(BaseModel):
    model: str
    output: list

@router.post("/hash")
async def generate_hash(payload: HashInput):
    data_str = payload.model + str(payload.output)
    hash_value = hashlib.sha256(data_str.encode()).hexdigest()
    return {"hash": hash_value}

@router.get("/count")
def get_count():
    try:
        count = contract.functions.getCount().call()
        return {"count": count}
    except Exception as e:
        return {"error": str(e)}

@router.get("/get/{index}")
def get_hash(index: int):
    try:
        hash_value = contract.functions.getHash(index).call()
        return {"index": index, "hash": hash_value}
    except Exception as e:
        return {"error": str(e)}
