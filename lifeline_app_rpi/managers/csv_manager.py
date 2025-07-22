import os
import pandas as pd
from threading import Lock

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
USERS_CSV = os.path.join(DATA_DIR, 'users.csv')
TESTS_CSV = os.path.join(DATA_DIR, 'tests.csv')

class CsvManager:
    _lock = Lock()

    @staticmethod
    def ensure_files():
        if not os.path.exists(USERS_CSV):
            pd.DataFrame(columns=['username','password_hash','email']).to_csv(USERS_CSV, index=False)
        if not os.path.exists(TESTS_CSV):
            pd.DataFrame(columns=['test_id','username','timestamp','glucose','value','status','iron','value','status','b12','value','status']).to_csv(TESTS_CSV, index=False)

    @staticmethod
    def read_users():
        CsvManager.ensure_files()
        with CsvManager._lock:
            return pd.read_csv(USERS_CSV)

    @staticmethod
    def write_users(df):
        with CsvManager._lock:
            df.to_csv(USERS_CSV, index=False)

    @staticmethod
    def read_tests():
        CsvManager.ensure_files()
        with CsvManager._lock:
            return pd.read_csv(TESTS_CSV)

    @staticmethod
    def write_tests(df):
        with CsvManager._lock:
            df.to_csv(TESTS_CSV, index=False)

    @staticmethod
    def add_user(username, password_hash, email=None):
        df = CsvManager.read_users()
        if username.lower() in [u.lower() for u in df['username']]:
            raise ValueError('Username already exists')
        new_row = {'username': username, 'password_hash': password_hash, 'email': email or ''}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        CsvManager.write_users(df)

    @staticmethod
    def update_user(username, **kwargs):
        df = CsvManager.read_users()
        idx = df.index[df['username'].str.lower() == username.lower()]
        if len(idx) == 0:
            raise ValueError('User not found')
        for k, v in kwargs.items():
            df.loc[idx, k] = v
        CsvManager.write_users(df)

    @staticmethod
    def delete_user(username):
        df = CsvManager.read_users()
        df = df[df['username'].str.lower() != username.lower()]
        CsvManager.write_users(df)

    @staticmethod
    def add_test(test_row):
        df = CsvManager.read_tests()
        df = pd.concat([df, pd.DataFrame([test_row])], ignore_index=True)
        CsvManager.write_tests(df)

    @staticmethod
    def get_user_tests(username):
        df = CsvManager.read_tests()
        return df[df['username'].str.lower() == username.lower()]