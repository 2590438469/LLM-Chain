import os

# Step 1: Read the content of r2E.rt file
r2E_file_path = 'stageResult/evaluator/r2E.rt'
with open(r2E_file_path, 'r') as file:
    p2E_content = file.read()

# Step 2: Format the string
formatted_string = f"{p2E_content}You are a evaluator of smart contract test cases, and the above test cases contain non-compliant ones. I need you to delete or modify them to comply with the specifications."

# Step 3: Save the formatted string to p3E.prompt
p3E_prompt_file_path = 'prompt/evaluator/p3E.prompt'
if not os.path.exists('prompt/evaluator'):
    os.makedirs('prompt/evaluator')

with open(p3E_prompt_file_path, 'w') as file:
    file.write(formatted_string)

print(f"Formatted string has been saved to {p3E_prompt_file_path}")
