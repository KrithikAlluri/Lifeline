"""
Model manager for local Gemma inference
"""

import os
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_PATH = "/Users/krithikalluri/Documents/GitHub/Lifeline/software/gemma3n_e2b_finetuned"

# Global model instances
tokenizer = None
model = None

def load_model():
    """Load the local Gemma model once at startup"""
    global tokenizer, model
    try:
        print("Loading local Gemma model...")
        tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_PATH,
            device_map="auto",     # or use "cpu" for fallback
            load_in_4bit=True      # Only if you quantized it!
        )
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Error loading model: {e}")
        # Fallback to CPU if GPU loading fails
        try:
            model = AutoModelForCausalLM.from_pretrained(
                MODEL_PATH,
                device_map="cpu",
                load_in_4bit=False
            )
            print("Model loaded on CPU as fallback")
        except Exception as e2:
            print(f"Failed to load model on CPU: {e2}")
            tokenizer = None
            model = None

def local_gemma_inference(messages):
    """Convert messages to prompt and run local inference"""
    if tokenizer is None or model is None:
        return "Error: Model not loaded. Please restart the application."
    
    try:
        # Convert messages to a single prompt string
        prompt_text = ""
        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            if role == "user":
                prompt_text += f"User: {content}\n"
            elif role == "assistant":
                prompt_text += f"Assistant: {content}\n"
        
        # Add the final assistant prompt
        prompt_text += "Assistant: "
        
        # Run inference
        inputs = tokenizer(prompt_text, return_tensors="pt").to(model.device)
        output = model.generate(
            **inputs, 
            max_new_tokens=256, 
            do_sample=True,
            temperature=0.7,
            pad_token_id=tokenizer.eos_token_id
        )
        reply = tokenizer.decode(output[0], skip_special_tokens=True)
        
        # Extract only the new response (remove the input prompt)
        if "Assistant: " in reply:
            reply = reply.split("Assistant: ")[-1].strip()
        
        return reply
        
    except Exception as e:
        return f"Error during inference: {str(e)}" 