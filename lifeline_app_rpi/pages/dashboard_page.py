from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout
from PyQt5.QtGui import QPixmap
from managers.csv_manager import CsvManager

class DashboardPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        # Add logo at the top
        self.logo_label = QLabel()
        pixmap = QPixmap('logo.jpg')
        if not pixmap.isNull():
            self.logo_label.setPixmap(pixmap.scaledToWidth(200))
            self.logo_label.setAlignment(Qt.AlignHCenter)
        layout.addWidget(self.logo_label)
        self.info_label = QLabel()
        layout.addWidget(self.info_label)
        layout.addWidget(QLabel("Recent Test Results:"))
        self.table = QTableWidget()
        layout.addWidget(self.table)
        # Two rows of buttons, spaced out
        btn_layout1 = QHBoxLayout()
        btn_layout1.addStretch()
        self.new_test_btn = QPushButton("Start New Test")
        self.new_test_btn.setFixedWidth(180)
        self.new_test_btn.setStyleSheet("margin: 0 16px; font-size: 18px;")
        self.new_test_btn.clicked.connect(self.goto_new_test)
        btn_layout1.addWidget(self.new_test_btn)
        btn_layout1.addStretch()
        self.export_btn = QPushButton("Export Data")
        self.export_btn.setFixedWidth(180)
        self.export_btn.setStyleSheet("margin: 0 16px; font-size: 18px;")
        btn_layout1.addWidget(self.export_btn)
        btn_layout1.addStretch()
        self.switch_btn = QPushButton("Switch User")
        self.switch_btn.setFixedWidth(180)
        self.switch_btn.setStyleSheet("margin: 0 16px; font-size: 18px;")
        self.switch_btn.clicked.connect(self.goto_login)
        btn_layout1.addWidget(self.switch_btn)
        btn_layout1.addStretch()
        btn_layout2 = QHBoxLayout()
        btn_layout2.addStretch()
        self.settings_btn = QPushButton("Settings/About")
        self.settings_btn.setFixedWidth(180)
        self.settings_btn.setStyleSheet("margin: 0 16px; font-size: 18px;")
        self.settings_btn.clicked.connect(self.goto_settings)
        btn_layout2.addWidget(self.settings_btn)
        btn_layout2.addStretch()
        self.chatbot_btn = QPushButton("Open Chatbot Page")
        self.chatbot_btn.setFixedWidth(180)
        self.chatbot_btn.setStyleSheet("margin: 0 16px; font-size: 18px;")
        self.chatbot_btn.clicked.connect(self.goto_chatbot)
        btn_layout2.addWidget(self.chatbot_btn)
        btn_layout2.addStretch()
        layout.addSpacing(32)
        layout.addLayout(btn_layout1)
        layout.addSpacing(24)
        layout.addLayout(btn_layout2)
        layout.addSpacing(32)
        self.setLayout(layout)

    def set_chatbot_button_visible(self, visible):
        self.chatbot_btn.setVisible(visible)

    def toggle_chatbot(self):
        self.parent.toggle_chatbot()

    def refresh(self):
        user = getattr(self.parent, 'current_user', None)
        if not user:
            self.info_label.setText("No user loaded.")
            return
        users = CsvManager.read_users()
        user_row = users[users['username'].str.lower() == user.lower()]
        if user_row.empty:
            self.info_label.setText("User not found.")
            return
        email = user_row.iloc[0]['email']
        self.info_label.setText(f"User: {user} | Email: {email if email else 'N/A'}")
        tests = CsvManager.get_user_tests(user)
        self.table.setRowCount(len(tests))
        self.table.setColumnCount(len(tests.columns))
        self.table.setHorizontalHeaderLabels(tests.columns)
        for i, row in tests.iterrows():
            for j, col in enumerate(tests.columns):
                self.table.setItem(i, j, QTableWidgetItem(str(row[col])))

    def goto_new_test(self):
        self.parent.show_new_test()

    def goto_login(self):
        self.parent.show_login()

    def goto_settings(self):
        self.parent.show_settings()

    def goto_chatbot(self):
        self.parent.show_chatbot()