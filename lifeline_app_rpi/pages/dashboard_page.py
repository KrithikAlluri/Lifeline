from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout
from managers.csv_manager import CsvManager

class DashboardPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.info_label = QLabel()
        layout.addWidget(self.info_label)
        layout.addWidget(QLabel("Recent Test Results:"))
        self.table = QTableWidget()
        layout.addWidget(self.table)
        btn_layout = QHBoxLayout()
        self.new_test_btn = QPushButton("Start New Test")
        self.new_test_btn.clicked.connect(self.goto_new_test)
        btn_layout.addWidget(self.new_test_btn)
        self.export_btn = QPushButton("Export Data")
        btn_layout.addWidget(self.export_btn)
        self.switch_btn = QPushButton("Switch User")
        self.switch_btn.clicked.connect(self.goto_login)
        btn_layout.addWidget(self.switch_btn)
        self.settings_btn = QPushButton("Settings/About")
        self.settings_btn.clicked.connect(self.goto_settings)
        btn_layout.addWidget(self.settings_btn)
        layout.addLayout(btn_layout)
        self.setLayout(layout)

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