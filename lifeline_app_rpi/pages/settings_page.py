from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QInputDialog
from managers.csv_manager import CsvManager
from managers.encryption_manager import EncryptionManager

APP_VERSION = "1.0.0"

class SettingsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.info_label = QLabel(f"Lifeline Blood Testing Kit App v{APP_VERSION}")
        layout.addWidget(self.info_label)
        layout.addWidget(QLabel("Change Password:"))
        self.old_pass = QLineEdit()
        self.old_pass.setEchoMode(QLineEdit.Password)
        self.old_pass.setPlaceholderText("Current Password")
        layout.addWidget(self.old_pass)
        self.new_pass = QLineEdit()
        self.new_pass.setEchoMode(QLineEdit.Password)
        self.new_pass.setPlaceholderText("New Password")
        layout.addWidget(self.new_pass)
        self.change_pass_btn = QPushButton("Change Password")
        self.change_pass_btn.clicked.connect(self.change_password)
        layout.addWidget(self.change_pass_btn)
        layout.addWidget(QLabel("Update Email:"))
        self.email_edit = QLineEdit()
        layout.addWidget(self.email_edit)
        self.update_email_btn = QPushButton("Update Email")
        self.update_email_btn.clicked.connect(self.update_email)
        layout.addWidget(self.update_email_btn)
        self.remove_email_btn = QPushButton("Remove Email")
        self.remove_email_btn.clicked.connect(self.remove_email)
        layout.addWidget(self.remove_email_btn)
        self.delete_btn = QPushButton("Delete User")
        self.delete_btn.clicked.connect(self.delete_user)
        layout.addWidget(self.delete_btn)
        self.back_btn = QPushButton("Back")
        self.back_btn.clicked.connect(self.goto_dashboard)
        layout.addWidget(self.back_btn)
        self.setLayout(layout)

    def refresh(self):
        user = getattr(self.parent, 'current_user', None)
        if not user:
            self.info_label.setText("No user loaded.")
            return
        users = CsvManager.read_users()
        user_row = users[users['username'].str.lower() == user.lower()]
        email = user_row.iloc[0]['email'] if not user_row.empty else ''
        self.email_edit.setText(email)

    def change_password(self):
        user = getattr(self.parent, 'current_user', None)
        if not user:
            return
        old = self.old_pass.text()
        new = self.new_pass.text()
        users = CsvManager.read_users()
        user_row = users[users['username'].str.lower() == user.lower()]
        if user_row.empty:
            self.show_error("User not found.")
            return
        if not EncryptionManager.check_password(old, user_row.iloc[0]['password_hash']):
            self.show_error("Incorrect current password.")
            return
        if not new or len(new) < 4:
            self.show_error("New password too short.")
            return
        CsvManager.update_user(user, password_hash=EncryptionManager.hash_password(new))
        QMessageBox.information(self, "Success", "Password changed.")
        self.old_pass.clear()
        self.new_pass.clear()

    def update_email(self):
        user = getattr(self.parent, 'current_user', None)
        if not user:
            return
        email = self.email_edit.text().strip()
        if email:
            from utils.validation_utils import is_valid_email
            if not is_valid_email(email):
                self.show_error("Invalid email.")
                return
        CsvManager.update_user(user, email=email)
        QMessageBox.information(self, "Success", "Email updated.")

    def remove_email(self):
        user = getattr(self.parent, 'current_user', None)
        if not user:
            return
        CsvManager.update_user(user, email='')
        QMessageBox.information(self, "Success", "Email removed.")
        self.email_edit.clear()

    def delete_user(self):
        user = getattr(self.parent, 'current_user', None)
        if not user:
            return
        pw, ok = QInputDialog.getText(self, "Confirm Password", "Enter password to delete user:", QLineEdit.Password)
        if not ok:
            return
        users = CsvManager.read_users()
        user_row = users[users['username'].str.lower() == user.lower()]
        if user_row.empty or not EncryptionManager.check_password(pw, user_row.iloc[0]['password_hash']):
            self.show_error("Incorrect password.")
            return
        CsvManager.delete_user(user)
        QMessageBox.information(self, "Deleted", "User deleted.")
        self.parent.current_user = None
        self.parent.show_login()

    def goto_dashboard(self):
        self.parent.show_dashboard()

    def show_error(self, msg):
        QMessageBox.warning(self, "Error", msg)