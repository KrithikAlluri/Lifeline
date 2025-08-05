import json
import re

input_path = 'Untitled.txt'
output_path = 'fixed_data.jsonl'

def extract_prompt_response(obj):
    prompt = None
    response = None

    print("---- New outer object ----")
    print(obj)

    # Try to extract from the dict's keys and values
    for k, v in obj.items():
        print("\nChecking key:", k[:80], "...")
        print("Checking value:", str(v)[:80], "...")
        # If k or v look like JSON strings, try to load them
        for item in (k, v):
            if isinstance(item, str) and item.strip().startswith('{'):
                try:
                    sub_obj = json.loads(item)
                    print("Decoded JSON from:", item[:80], "...")
                    # Look for prompt and response inside
                    if isinstance(sub_obj, dict):
                        if 'prompt' in sub_obj and not prompt:
                            prompt = sub_obj['prompt']
                            print("  -> Found prompt:", prompt)
                        if 'response' in sub_obj and not response:
                            response = sub_obj['response']
                            print("  -> Found response:", response)
                except Exception as e:
                    print("    [Error decoding JSON]:", e)
            elif isinstance(item, str):
                # If string contains something like "response": "..."
                m = re.search(r'"response":\s*"(.+?)(?<!\\)"', item)
                if m and not response:
                    response = m.group(1)
                    print("  -> Found response (regex):", response)
        # Fallback for prompt: if the key is just 'prompt'
        if k == 'prompt' and not prompt:
            prompt = v
            print("  -> Found prompt (key):", prompt)
        if k == 'response' and not response:
            response = v
            print("  -> Found response (key):", response)
    print("Resulting prompt:", prompt)
    print("Resulting response:", response)
    return prompt, response

with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
    for i, line in enumerate(infile):
        print(f"\n### Processing line {i+1} ###")
        try:
            outer = json.loads(line.strip())
        except Exception as e:
            print(f"Could not decode line {i+1}:", e)
            continue

        if not isinstance(outer, dict):
            print("Not a dict, skipping.")
            continue

        prompt, response = extract_prompt_response(outer)
        # Fallback: If no prompt found, try first JSON key as prompt, and search value for response
        if not prompt:
            for k in outer:
                try:
                    sub_obj = json.loads(k)
                    if isinstance(sub_obj, dict) and 'prompt' in sub_obj:
                        prompt = sub_obj['prompt']
                        print("Fallback prompt (first key):", prompt)
                        break
                except Exception as e:
                    print("Error loading fallback prompt:", e)
                    continue

        if prompt and response:
            obj = {"prompt": prompt, "response": response}
            print("WRITING:", obj)
            outfile.write(json.dumps(obj, ensure_ascii=False) + "\n")
        else:
            print("Skipping line, no complete prompt/response.")