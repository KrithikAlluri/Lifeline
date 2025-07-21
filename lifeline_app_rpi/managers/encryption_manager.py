import hashlib

class EncryptionManager:
    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    @staticmethod
    def check_password(password: str, password_hash: str) -> bool:
        return EncryptionManager.hash_password(password) == password_hash
