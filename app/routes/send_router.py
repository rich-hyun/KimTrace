from fastapi import APIRouter
from pydantic import BaseModel
from app.services.blockchain_service import send_hash_to_blockchain

router = APIRouter()

class HashInput(BaseModel):
    hash: str

@router.post("/send")
def send_hash(input: HashInput):
    tx_hash = send_hash_to_blockchain(input.hash)
    return {"tx_hash": tx_hash}
