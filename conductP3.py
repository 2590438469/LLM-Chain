import os

p2_result_file_path = 'stageResult/p2.rt'
prompt_folder_path = 'prompt'
prompt_file_name = 'p3.prompt'

with open(p2_result_file_path, 'r') as file:
    p2_result = file.read()

final_prompt = f"{p2_result}\nPlease double-check the format of the generated test cases based on the template provided by me; the address type data should be a 40-character hexadecimal string like :\"0x1285774956032651954812857749560326519548\"."

if not os.path.exists(prompt_folder_path):
    os.makedirs(prompt_folder_path)

prompt_file_path = os.path.join(prompt_folder_path, prompt_file_name)
with open(prompt_file_path, 'w') as file:
    file.write(final_prompt)

print(f"finish:{prompt_file_path}")