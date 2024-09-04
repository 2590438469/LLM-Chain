import os

# Step 1: Read the content of r1E.rt file
r1E_file_path = 'stageResult/evaluator/r1E.rt'
with open(r1E_file_path, 'r') as file:
    p1E_content = file.read()

# Step 2: Format the string
formatted_string = f"{p1E_content}You are a evaluator of smart contract test cases, and the above test cases do not achieve 100% coverage. Therefore, I need you to generate more test cases based on the test cases and source code provided by me to achieve 100% instruction coverage for the test case set."

# Step 3: Save the formatted string to p2E.prompt
p2E_prompt_file_path = 'prompt/evaluator/p2E.prompt'
if not os.path.exists('prompt/evaluator'):
    os.makedirs('prompt/evaluator')

with open(p2E_prompt_file_path, 'w') as file:
    file.write(formatted_string)

print(f"Formatted string has been saved to {p2E_prompt_file_path}")
