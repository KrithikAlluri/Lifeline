from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class SettingsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Settings / About'))
        self.change_password_button = QPushButton('Change Password')
        layout.addWidget(self.change_password_button)
        self.update_email_button = QPushButton('Update Email')
        layout.addWidget(self.update_email_button)
        self.delete_user_button = QPushButton('Delete User')
        layout.addWidget(self.delete_user_button)
        self.app_info_label = QLabel('Lifeline App v1.0')
        layout.addWidget(self.app_info_label)
        self.setLayout(layout)
