from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class DashboardPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Dashboard'))
        self.user_info_label = QLabel('User info here')
        layout.addWidget(self.user_info_label)
        self.recent_results_label = QLabel('Recent test results here')
        layout.addWidget(self.recent_results_label)
        self.new_test_button = QPushButton('Start New Test')
        layout.addWidget(self.new_test_button)
        self.export_button = QPushButton('Export Data')
        layout.addWidget(self.export_button)
        self.switch_user_button = QPushButton('Switch User')
        layout.addWidget(self.switch_user_button)
        self.settings_button = QPushButton('Settings/About')
        layout.addWidget(self.settings_button)
        self.setLayout(layout)
