from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model, PeftModel
from huggingface_hub import login
import os
import torch
import timm
# hf token: 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
model_id = "google/gemma-3n-E2B-it"

hf_token = os.getenv("HF_TOKEN")
if hf_token:
    login(token=hf_token)

tokenizer = AutoTokenizer.from_pretrained(model_id, token=hf_token)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map={"": "mps"},
    token=hf_token,
)

lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)

model = get_peft_model(model, lora_config)

def preprocess(example):
    prompt = example["prompt"]
    response = example["response"]
    # Tokenize prompt and response separately
    prompt_enc = tokenizer(
        prompt,
        truncation=True,
        padding="max_length",
        max_length=512,
        add_special_tokens=False
    )
    response_enc = tokenizer(
        response,
        truncation=True,
        padding="max_length",
        max_length=256,
        add_special_tokens=False
    )
    # Build input_ids: prompt + response, padded to 512
    input_ids = prompt_enc["input_ids"] + response_enc["input_ids"]
    input_ids = input_ids[:512]
    input_ids += [tokenizer.pad_token_id] * (512 - len(input_ids))
    # Build labels: -100 for prompt, real tokens for response
    labels = [-100] * len(prompt_enc["input_ids"]) + response_enc["input_ids"]
    labels = labels[:512]
    labels += [-100] * (512 - len(labels))
    return {
        "input_ids": input_ids,
        "labels": labels
    }

ds = load_dataset("json", data_files="fixed_data.jsonl", split="train")
ds = ds.map(preprocess, batched=False)

training_args = TrainingArguments(
    per_device_train_batch_size=1,
    gradient_accumulation_steps=8,
    learning_rate=2e-4,
    num_train_epochs=4,
    output_dir="./gemma3n_e2b_qlora",
    logging_steps=10,
    save_strategy="epoch",
    save_total_limit=2,
    # fp16=True,
    report_to="none",
)

trainer = Trainer(model=model, args=training_args, train_dataset=ds)
trainer.train()

model.save_pretrained("./gemma3n_e2b_qlora_adapter")
tokenizer.save_pretrained("./gemma3n_e2b_qlora_adapter")

base = AutoModelForCausalLM.from_pretrained(model_id, token=hf_token)
adapter = PeftModel.from_pretrained(base, "./gemma3n_e2b_qlora_adapter")
merged = adapter.merge_and_unload()
merged.save_pretrained("./gemma3n_e2b_finetuned")
tokenizer.save_pretrained("./gemma3n_e2b_finetuned")