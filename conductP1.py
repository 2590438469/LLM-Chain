import os

solidity_file_path = 'solidity/testcode.sol'
prompt_folder_path = 'prompt/generator'
prompt_file_name = 'p1.prompt'

with open(solidity_file_path, 'r') as file:
    contract_code = file.read()

task_prompt = f"{contract_code}\nHere is my smart contract, please generate a sufficient number of test cases to cover all functions, branches, and statements."

if not os.path.exists(prompt_folder_path):
    os.makedirs(prompt_folder_path)

prompt_file_path = os.path.join(prompt_folder_path, prompt_file_name)
with open(prompt_file_path, 'w') as file:
    file.write(task_prompt)

print(f"finish:{prompt_file_path}")