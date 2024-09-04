import time
import os
from openai import OpenAI

client = OpenAI(api_key="sk-qvp49C0zJlPLkJ8io7yI1IWe5a9M9r0xJhTy7dkciNJj02ON")

completion_tokens = 0
prompt_tokens = 0

def gpt(prompt, model, temperature=0.7, max_tokens=4000, n=1, stop=None) -> list:
    messages = [{"role": "user", "content": prompt}]
    if model == "gpt-4":
        time.sleep(30)
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

        completion_tokens += res.usage.completion_tokens
        prompt_tokens += res.usage.prompt_tokens
    return outputs

prompt_file_path = 'prompt/evaluator/p3E.prompt'
with open(prompt_file_path, 'r') as file:
    p1_prompt_content = file.read()

model = "gpt-4"
response = gpt(prompt=p1_prompt_content, model=model)

stage_result_folder_path = 'stageResult/evaluator'
if not os.path.exists(stage_result_folder_path):
    os.makedirs(stage_result_folder_path)

result_file_path = os.path.join(stage_result_folder_path, 'p3E.rt')
with open(result_file_path, 'w') as file:
    file.write("\n".join(response))

print(f"finish:{result_file_path}")