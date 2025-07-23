import random, json

biomarkers = {
    "Glucose": {
        "unit": "mg/dL",
        "ranges": {"low": (50, 69), "normal": (70, 99), "high": (126, 200)},
        "responses": {
            "low": "Glucose is low (<70 mg/dL): dizziness or confusion may occur—eat fast-acting carbs and monitor yourself.",
            "normal": "Glucose is normal (70–99 mg/dL).",
            "high": "Glucose is high (≥126 mg/dL fasting): this could indicate diabetes—consult a healthcare provider."
        }
    },
    "Iron": {
        "unit": "µg/dL",
        "ranges": {"low": (30, 59), "normal": (60, 170), "high": (171, 250)},
        "responses": {
            "low": "Iron is low (<60 µg/dL): fatigue or anemia could develop—consider iron-rich foods and check with a doctor.",
            "normal": "Iron is normal (60–170 µg/dL).",
            "high": "Iron is high (>170 µg/dL): this might indicate an overload or metabolic issue—seek medical advice."
        }
    },
    "Vitamin B12": {
        "unit": "pg/mL",
        "ranges": {"low": (100, 199), "normal": (200, 900), "high": (901, 1200)},
        "responses": {
            "low": "Vitamin B12 is low (<200 pg/mL): you may experience fatigue or neuropathy—consider supplements and testing metabolic markers.",
            "normal": "Vitamin B12 is normal (200–900 pg/mL).",
            "high": "Vitamin B12 is high (>900 pg/mL): usually not harmful but review supplement intake."
        }
    },
    "Total Protein": {
        "unit": "g/dL",
        "ranges": {"low": (4.0, 6.2), "normal": (6.3, 8.3), "high": (8.4, 10.0)},
        "responses": {
            "low": "Total protein is low (<6.3 g/dL): could indicate malnutrition or liver/kidney issues—seek medical attention.",
            "normal": "Total protein is normal (6.3–8.3 g/dL).",
            "high": "Total protein is high (>8.3 g/dL): possible dehydration or inflammation—consult your provider."
        }
    },
    "pH": {
        "unit": "",
        "ranges": {"low": (7.0, 7.34), "normal": (7.35, 7.45), "high": (7.46, 7.60)},
        "responses": {
            "low": "Blood pH is low (<7.35): this indicates acidosis—urgent medical evaluation is needed.",
            "normal": "Blood pH is normal (7.35–7.45).",
            "high": "Blood pH is high (>7.45): this suggests alkalosis—medical advice is recommended."
        }
    },
    "CRP": {
        "unit": "mg/L",
        "ranges": {"low": (0, 0.99), "normal": (1.0, 3.0), "high": (3.1, 20.0)},
        "responses": {
            "low": "CRP is low (<1 mg/L): minimal inflammation detected.",
            "normal": "CRP is normal (1–3 mg/L): some inflammation is normal.",
            "high": "CRP is high (>3 mg/L): active inflammation or infection—consult a doctor."
        }
    },
    "Ketones": {
        "unit": "mmol/L",
        "ranges": {"low": (0.0, 0.39), "normal": (0.4, 1.5), "high": (1.6, 5.0)},
        "responses": {
            "low": "Ketones are low (<0.4 mmol/L): normal for most individuals.",
            "normal": "Ketones are normal (0.4–1.5 mmol/L).",
            "high": "Ketones are high (>1.5 mmol/L): ketosis or ketoacidosis risk—monitor closely."
        }
    },
    "Lactate": {
        "unit": "mmol/L",
        "ranges": {"low": (0.0, 0.49), "normal": (0.5, 2.2), "high": (2.3, 10.0)},
        "responses": {
            "low": "Lactate is low (<0.5 mmol/L): generally not concerning.",
            "normal": "Lactate is normal (0.5–2.2 mmol/L).",
            "high": "Lactate is high (>2.2 mmol/L): may indicate tissue stress—see a doctor."
        }
    },
    "Sodium": {
        "unit": "mmol/L",
        "ranges": {"low": (120, 134), "normal": (135, 145), "high": (146, 160)},
        "responses": {
            "low": "Sodium is low (<135 mmol/L): hyponatremia—risk of headache or confusion—seek medical care.",
            "normal": "Sodium is normal (135–145 mmol/L).",
            "high": "Sodium is high (>145 mmol/L): hypernatremia may cause dehydration—consult your doctor."
        }
    },
    "Potassium": {
        "unit": "mmol/L",
        "ranges": {"low": (2.0, 3.49), "normal": (3.5, 5.2), "high": (5.3, 7.0)},
        "responses": {
            "low": "Potassium is low (<3.5 mmol/L): hypokalemia—may cause weakness or arrhythmias—medical evaluation needed.",
            "normal": "Potassium is normal (3.5–5.2 mmol/L).",
            "high": "Potassium is high (>5.2 mmol/L): hyperkalemia—potential heart risk—seek urgent care."
        }
    }
}

def generate_samples(n=1000):
    dataset = []
    for _ in range(n):
        user_vals, assistant_msgs = [], []
        for name, info in biomarkers.items():
            state = random.choice(list(info["ranges"].keys()))
            lo, hi = info["ranges"][state]
            val = round(random.uniform(lo, hi),2)
            user_vals.append(f"{name}: {val} {info['unit']}".strip())
            assistant_msgs.append(info["responses"][state])
        user_text = "Here are my results: " + "; ".join(user_vals) + "."
        assistant_text = " ".join(assistant_msgs)
        dataset.append({
            "messages":[
                {"role":"user","content":user_text},
                {"role":"assistant","content":assistant_text}
            ]
        })
    with open("lifeline_dataset.jsonl","w") as f:
        for entry in dataset:
            f.write(json.dumps(entry)+"\n")
    return dataset

# generate 2000 samples:
print(generate_samples(2000))
print("✅ Generated lifeline_dataset.jsonl with 2000 samples")