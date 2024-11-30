import os
from web3 import Web3

CONTRACTS_FOLDER_PATH = 'contracts_folder'  
ETHEREUM_RPC_URL = ''  
LINE_THRESHOLD = 100  
TRANSACTION_THRESHOLD = 10  


w3 = Web3(Web3.HTTPProvider(ETHEREUM_RPC_URL))

def get_code_lines(contract_file_path):
    with open(contract_file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)

def get_contract_transactions(contract_address):
    try:
        contract = w3.eth.contract(address=contract_address, abi=[])
        transactions = w3.eth.getTransactionCount(contract_address)
        return transactions
    except Exception as e:
        print(f"can't get contract {contract_address} data: {e}")
        return 0

def is_toy_contract(contract_file_path, contract_address):
    code_lines = get_code_lines(contract_file_path)
    transaction_count = get_contract_transactions(contract_address)
    
    if code_lines < LINE_THRESHOLD or transaction_count < TRANSACTION_THRESHOLD:
        return True
    return False

def filter_toy_contracts(directory):
    toy_contracts = []
    
    for filename in os.listdir(directory):
        contract_file_path = os.path.join(directory, filename)

        if contract_file_path.endswith('.sol'):
            contract_address = "0x..."  
            
            if is_toy_contract(contract_file_path, contract_address):
                toy_contracts.append(contract_file_path)
    
    return toy_contracts

def main():
    toy_contracts = filter_toy_contracts(CONTRACTS_FOLDER_PATH)
    
    print("toy contract:")
    for contract in toy_contracts:
        print(contract)

if __name__ == '__main__':
    main()
