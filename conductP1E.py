import os

# Step 1: Read the content of r3new.rt file
r3new_file_path = 'stageResult/generator/r3new.rt'
with open(r3new_file_path, 'r') as file:
    p3_content = file.read()

# Step 2: Format the string
formatted_string = f"{p3_content},Remove the test cases with the same execution path, and return the original prompt text if not."

# Step 3: Save the formatted string to p1E.prompt
evaluator_folder_path = 'prompt/evaluator'
if not os.path.exists(evaluator_folder_path):
    os.makedirs(evaluator_folder_path)

p1E_prompt_file_path = os.path.join(evaluator_folder_path, 'p1E.prompt')
with open(p1E_prompt_file_path, 'w') as file:
    file.write(formatted_string)

print(f"Formatted string has been saved to {p1E_prompt_file_path}")