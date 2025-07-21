from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from managers.csv_manager import CsvManager
from managers.encryption_manager import EncryptionManager
from utils.validation_utils import is_valid_email, is_valid_username

class CreateUserPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Name:"))
        self.name_edit = QLineEdit()
        layout.addWidget(self.name_edit)
        layout.addWidget(QLabel("Password:"))
        self.pass_edit = QLineEdit()
        self.pass_edit.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.pass_edit)
        layout.addWidget(QLabel("Confirm Password:"))
        self.confirm_edit = QLineEdit()
        self.confirm_edit.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.confirm_edit)
        layout.addWidget(QLabel("Email (optional):"))
        self.email_edit = QLineEdit()
        layout.addWidget(self.email_edit)
        self.create_btn = QPushButton("Create User")
        self.create_btn.clicked.connect(self.create_user)
        layout.addWidget(self.create_btn)
        self.back_btn = QPushButton("Back")
        self.back_btn.clicked.connect(self.goto_login)
        layout.addWidget(self.back_btn)
        self.setLayout(layout)

    def create_user(self):
        name = self.name_edit.text().strip()
        password = self.pass_edit.text()
        confirm = self.confirm_edit.text()
        email = self.email_edit.text().strip()
        if not is_valid_username(name):
            self.show_error("Invalid username. Use 3-32 alphanumeric characters.")
            return
        if not password or len(password) < 4:
            self.show_error("Password must be at least 4 characters.")
            return
        if password != confirm:
            self.show_error("Passwords do not match.")
            return
        if email and not is_valid_email(email):
            self.show_error("Invalid email address.")
            return
        try:
            CsvManager.add_user(name, EncryptionManager.hash_password(password), email)
        except ValueError as e:
            self.show_error(str(e))
            return
        QMessageBox.information(self, "Success", "User created!")
        self.goto_login()

    def goto_login(self):
        self.parent.show_login()

    def show_error(self, msg):
        QMessageBox.warning(self, "Create User Failed", msg)