from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_dir = "./gemma3n_e2b_finetuned"
device = "mps" if torch.backends.mps.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForCausalLM.from_pretrained(
    model_dir,
    torch_dtype=torch.float16 if device == "mps" else torch.float32,
    device_map={"": device}
)

prompt = """Age: 44
Sex: Female
Weight: 59 kg
Height: 162 cm
Smoking: No
Alcohol: Daily
Exercise: Rarely
Diet: Omnivore
Medical Conditions: None
Medications: None

Blood test results:
Glucose: 98 mg/dL
Creatinine: 0.7 mg/dL
Urea: 23 mg/dL
Potassium: 4.0 mmol/L
Albumin: 4.5 g/dL
Hemoglobin: 13.9 g/dL
Uric Acid: 4.6 mg/dL
Vitamin B12: 460 pg/mL

What do these blood test results mean for me?
"""

params_grid = [
    {"temperature": 0.7, "top_p": 0.95, "top_k": 40, "max_new_tokens": 128},
    {"temperature": 1.0, "top_p": 0.85, "top_k": 50, "max_new_tokens": 128},
    {"temperature": 0.4, "top_p": 0.99, "top_k": 30, "max_new_tokens": 256},
    {"temperature": 1.3, "top_p": 0.9,  "top_k": 70, "max_new_tokens": 128},
]

inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=512).to(device)

with torch.no_grad():
    for idx, params in enumerate(params_grid):
        print("\n" + "=" * 30)
        print(f"Params set {idx+1}: {params}")
        output = model.generate(
            **inputs,
            max_new_tokens=params["max_new_tokens"],
            do_sample=True,
            top_p=params["top_p"],
            top_k=params["top_k"],
            temperature=params["temperature"],
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.eos_token_id
        )
        generated = tokenizer.decode(output[0], skip_special_tokens=True)
        print(generated)
        print("=" * 30 + "\n")

print("All generations done.")