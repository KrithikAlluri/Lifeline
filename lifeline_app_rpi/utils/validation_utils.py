import validators
import os
import pandas as pd

def is_valid_email(email: str) -> bool:
    return validators.email(email)

def is_valid_username(username: str) -> bool:
    return username and username.isalnum() and 3 <= len(username) <= 32

def check_csv_integrity(path: str, required_columns: list) -> bool:
    if not os.path.exists(path):
        return False
    try:
        df = pd.read_csv(path)
        return all(col in df.columns for col in required_columns)
    except Exception:
        return False