from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = FastAPI()

# path
model_path = "/root/autodl-tmp/Models/deepseek-r1-1.5b-merged"

# tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True).cuda()

# PromptRequest
class PromptRequest(BaseModel):
    prompt: str

# POST接口
@app.post("/generate")
async def generate_text(request: PromptRequest):
    prompt = request.prompt
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    outputs = model.generate(
        inputs["input_ids"],
        max_length=200
    )

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {"generated_text": generated_text}