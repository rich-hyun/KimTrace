from fastapi import APIRouter
from app.services.blockchain_service import contract
from web3 import Web3

router = APIRouter()

@router.get("/hashes", tags=["Blockchain"], summary="Get all stored hashes from smart contract")
def get_all_hashes():
    try:
        count = contract.functions.getCount().call()
        result = []
        for i in range(count):
            hash_value = contract.functions.getHash(i).call()
            result.append({
                "index": i,
                "hash": hash_value
            })
        return result
    except Exception as e:
        return {"error": str(e)}
