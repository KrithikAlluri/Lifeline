from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox
from managers.csv_manager import CsvManager
from managers.encryption_manager import EncryptionManager

class LoginPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Select User:"))
        self.user_combo = QComboBox()
        self.refresh_users()
        layout.addWidget(self.user_combo)
        layout.addWidget(QLabel("Password:"))
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_edit)
        self.login_btn = QPushButton("Login")
        self.login_btn.clicked.connect(self.try_login)
        layout.addWidget(self.login_btn)
        self.create_btn = QPushButton("Create New User")
        self.create_btn.clicked.connect(self.goto_create_user)
        layout.addWidget(self.create_btn)
        self.setLayout(layout)

    def refresh_users(self):
        self.user_combo.clear()
        users = CsvManager.read_users()
        for u in users['username']:
            self.user_combo.addItem(u)

    def try_login(self):
        username = self.user_combo.currentText()
        password = self.password_edit.text()
        users = CsvManager.read_users()
        user_row = users[users['username'].str.lower() == username.lower()]
        if user_row.empty:
            self.show_error("User not found.")
            return
        password_hash = user_row.iloc[0]['password_hash']
        if not EncryptionManager.check_password(password, password_hash):
            self.show_error("Incorrect password.")
            return
        self.password_edit.clear()
        self.parent.show_dashboard()

    def goto_create_user(self):
        self.parent.show_create_user()

    def show_error(self, msg):
        QMessageBox.warning(self, "Login Failed", msg)