from fastapi import APIRouter
from pydantic import BaseModel
from app.services.blockchain_service import send_hash_to_blockchain

router = APIRouter()

class HashInput(BaseModel):
    hash: str

@router.post(
    "/send",
    tags=["Blockchain"],
    summary="Send hash to smart contract and return tx hash"
)
def send_hash(input: HashInput):
    tx_hash = send_hash_to_blockchain(input.hash)
    return {"tx_hash": tx_hash}

@router.get("/tx/{index}")
def get_tx_by_index(index: int):
    try:
        hash_value = get_hash_by_index(index)  # 스마트컨트랙트에서 hash 가져오기
        etherscan_link = f"https://sepolia.etherscan.io/tx/{hash_value}"
        return {"hash": hash_value, "etherscan_link": etherscan_link}
    except Exception as e:
        return {"error": str(e)}
