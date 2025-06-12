from web3 import Web3

# 📌 여기를 본인의 정보로 바꿔주세요
RPC_URL = "https://sepolia.infura.io/v3/0ae21d24a8a94d5489b96a7ec83ea22e"
CONTRACT_ADDRESS = "0xed93f6c89fba8db6d1589a37387327da41114a25"
PRIVATE_KEY = "942096d9cbe7aceceb7ab52411113754b0c0c7e274b888b3ba7f521d8cda14b5"
SENDER_ADDRESS = "0x92A19C66448154955A24601a25f1E9E758e7a40d"
ABI = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_hash",
				"type": "string"
			}
		],
		"name": "storeHash",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "index",
				"type": "uint256"
			}
		],
		"name": "getHash",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "hashes",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]  # Remix에서 복사한 ABI 전체 붙여넣기

# ✅ Web3 연결
w3 = Web3(Web3.HTTPProvider(RPC_URL))
contract = w3.eth.contract(
    address=w3.to_checksum_address(CONTRACT_ADDRESS),
    abi=ABI
)

def send_hash_to_blockchain(hash_str: str):
    nonce = w3.eth.get_transaction_count(SENDER_ADDRESS)

    txn = contract.functions.storeHash(hash_str).build_transaction({
        'from': SENDER_ADDRESS,
        'nonce': nonce,
        'gas': 200000,
        'gasPrice': w3.to_wei('30', 'gwei')
    })

    signed_txn = w3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)

    return w3.to_hex(tx_hash)

def get_transaction_hash_by_index(index: int) -> str:
    tx_receipt = contract.functions.getHash(index).call()
    return tx_receipt
