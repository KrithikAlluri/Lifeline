import os
import csv
from threading import Lock

class CsvManager:
    def __init__(self, users_csv, tests_csv):
        self.users_csv = users_csv
        self.tests_csv = tests_csv
        self.lock = Lock()
        self._ensure_files()

    def _ensure_files(self):
        os.makedirs(os.path.dirname(self.users_csv), exist_ok=True)
        if not os.path.exists(self.users_csv):
            with open(self.users_csv, 'w', encoding='utf-8') as f:
                f.write('username,password_hash,email\n')
        if not os.path.exists(self.tests_csv):
            with open(self.tests_csv, 'w', encoding='utf-8') as f:
                f.write('test_id,username,timestamp\n')

    def get_users(self):
        with self.lock, open(self.users_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)

    def add_user(self, username, password_hash, email=None):
        # TODO: Enforce unique username, append user
        pass

    def get_tests(self, username=None):
        with self.lock, open(self.tests_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            if username:
                return [row for row in reader if row['username'] == username]
            return list(reader)

    def add_test(self, test_data):
        # TODO: Append test row
        pass
