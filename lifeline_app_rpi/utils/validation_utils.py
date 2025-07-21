import re

def is_valid_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def is_valid_username(username: str) -> bool:
    return username and username.isalnum() and len(username) >= 3
