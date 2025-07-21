import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QDockWidget
from PyQt5.QtCore import Qt
# Import page stubs (to be implemented)
from pages.login_page import LoginPage
from pages.create_user_page import CreateUserPage
from pages.dashboard_page import DashboardPage
from pages.new_test_wizard_page import NewTestWizardPage
from pages.results_page import ResultsPage
from pages.settings_page import SettingsPage
from chatbot.chatbot_widget import ChatbotWidget

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
USERS_CSV = os.path.join(DATA_DIR, 'users.csv')
TESTS_CSV = os.path.join(DATA_DIR, 'tests.csv')

# Ensure data directory and CSVs exist
def ensure_csv_files():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(USERS_CSV):
        with open(USERS_CSV, 'w', encoding='utf-8') as f:
            f.write('username,password_hash,email\n')
    if not os.path.exists(TESTS_CSV):
        with open(TESTS_CSV, 'w', encoding='utf-8') as f:
            f.write('test_id,username,timestamp\n')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Lifeline Blood Testing Kit')
        self.setGeometry(100, 100, 800, 480)  # 5" touchscreen size
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Instantiate pages (to be implemented)
        self.login_page = LoginPage(self)
        self.create_user_page = CreateUserPage(self)
        self.dashboard_page = DashboardPage(self)
        self.new_test_wizard_page = NewTestWizardPage(self)
        self.results_page = ResultsPage(self)
        self.settings_page = SettingsPage(self)

        # Add pages to stack
        self.stack.addWidget(self.login_page)           # index 0
        self.stack.addWidget(self.create_user_page)     # index 1
        self.stack.addWidget(self.dashboard_page)       # index 2
        self.stack.addWidget(self.new_test_wizard_page) # index 3
        self.stack.addWidget(self.results_page)         # index 4
        self.stack.addWidget(self.settings_page)        # index 5

        # Set up chatbot dock (stub)
        self.chatbot_dock = QDockWidget('Chatbot', self)
        self.chatbot_widget = ChatbotWidget(self)
        self.chatbot_dock.setWidget(self.chatbot_widget)
        self.chatbot_dock.setAllowedAreas(Qt.RightDockWidgetArea | Qt.BottomDockWidgetArea)
        self.addDockWidget(Qt.RightDockWidgetArea, self.chatbot_dock)
        self.chatbot_dock.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)

        # Show login page by default
        self.stack.setCurrentIndex(0)

        # TODO: Connect navigation signals between pages

if __name__ == '__main__':
    ensure_csv_files()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
