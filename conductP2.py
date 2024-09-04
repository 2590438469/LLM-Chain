import os
import re

solidity_file_path = 'solidity/testcode.sol'
contextual_info_file_path = 'solidity/contextual_information.txt'
json_format_file_path = 'solidity/json_format.txt'
prompt_folder_path = 'prompt/generator'
prompt_file_name = 'p2.prompt'

with open(solidity_file_path, 'r') as file:
    contract_code = file.read()

header_comment_match = re.search(r'(/\*.*?\*/)', contract_code, re.DOTALL)
header_comment = header_comment_match.group(1) if header_comment_match else ''

with open(contextual_info_file_path, 'r') as file:
    contextual_information = file.read()

with open(json_format_file_path, 'r') as file:
    json_format = file.read()

context_and_json = f"{header_comment}\n{contextual_information},we need you to generate test cases according to the following template:{json_format}."

if not os.path.exists(prompt_folder_path):
    os.makedirs(prompt_folder_path)

prompt_file_path = os.path.join(prompt_folder_path, prompt_file_name)
with open(prompt_file_path, 'w') as file:
    file.write(context_and_json)

print(f"finish:{prompt_file_path}")