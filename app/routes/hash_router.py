from fastapi import APIRouter
from pydantic import BaseModel
import hashlib
from fastapi import HTTPException
from app.services.blockchain_service import contract


router = APIRouter()

class HashInput(BaseModel):
    model: str
    output: list

@router.post(
    "/hash",
    tags=["Hash"],
    summary="Generate SHA256 hash"
)
async def generate_hash(payload: HashInput):
    data_str = payload.model + str(payload.output)
    hash_value = hashlib.sha256(data_str.encode()).hexdigest()
    return {"hash": hash_value}

@router.get(
    "/count",
    tags=["Blockchain"],
    summary="Get number of stored hashes on-chain"
)
def get_count():
    try:
        count = contract.functions.getCount().call()
        return {"count": count}
    except Exception as e:
        return {"error": str(e)}

@router.get(
    "/get/{index}",
    tags=["Blockchain"],
    summary="Retrieve hash by index from smart contract"
)
def get_hash(index: int):
    try:
        hash_value = contract.functions.getHash(index).call()
        return {"index": index, "hash": hash_value}
    except Exception as e:
        return {"error": str(e)}

@router.get(
    "/tx/{index}",
    tags=["Blockchain"],
    summary="Get transaction hash and Etherscan link"
)
def get_tx_by_index(index: int):
    try:
        tx_hash = contract.functions.getHash(index).call()
        etherscan_url = f"https://sepolia.etherscan.io/tx/{tx_hash}"
        return {"tx_hash": tx_hash, "etherscan_url": etherscan_url}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
