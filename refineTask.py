import time
import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key="sk-qvp49C0zJlPLkJ8io7yI1IWe5a9M9r0xJhTy7dkciNJj02ON")

completion_tokens = 0
prompt_tokens = 0

# Define the gpt and chatgpt functions
def gpt(prompt, model, temperature=0.7, max_tokens=4000, n=1, stop=None) -> list:
    messages = [{"role": "user", "content": prompt}]
    if model == "gpt-4":
        time.sleep(30)  # Prevent speed limitation exception
    return chatgpt(messages, model=model, temperature=temperature, max_tokens=max_tokens, n=n, stop=stop)

def chatgpt(messages, model, temperature, max_tokens, n, stop) -> list:
    global completion_tokens, prompt_tokens
    outputs = []
    while n > 0:
        cnt = min(n, 20)
        n -= cnt
        res = client.chat.completions.create(model=model, messages=messages, temperature=temperature, max_tokens=max_tokens,
                                             n=cnt, stop=stop)
        outputs.extend([choice["message"]["content"] for choice in res.choices])
        # Log token usage
        completion_tokens += res.usage.completion_tokens
        prompt_tokens += res.usage.prompt_tokens
    return outputs

# Read the content of p1.rt file
p1_result_file_path = 'stageResult/generator/p1.rt'
with open(p1_result_file_path, 'r') as file:
    p1_content = file.read()

# Format the prompt string
formatted_prompt = f"{p1_content}, here is a prompt provided by me, please improve the vocabulary and sentences"

# Request LLM to generate the optimized prompt
model = "gpt-4"  # You can change the model if needed
response = gpt(prompt=formatted_prompt, model=model)

# Save the generated response to the p1new.rt file
prompt_folder_path = 'prompt/generator'
if not os.path.exists(prompt_folder_path):
    os.makedirs(prompt_folder_path)

new_prompt_file_path = os.path.join(prompt_folder_path, 'p1new.rt')
with open(new_prompt_file_path, 'w') as file:
    file.write("\n".join(response))

print(f"Optimized prompt has been saved to {new_prompt_file_path}")