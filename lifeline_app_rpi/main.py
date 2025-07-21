import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QDockWidget
from PyQt5.QtCore import Qt

# Import pages (to be implemented)
from pages.login_page import LoginPage
from pages.create_user_page import CreateUserPage
from pages.dashboard_page import DashboardPage
from pages.new_test_wizard_page import NewTestWizardPage
from pages.results_page import ResultsPage
from pages.settings_page import SettingsPage
from chatbot.chatbot_widget import ChatbotWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lifeline Blood Testing Kit")
        self.setMinimumSize(800, 480)
        self.setStyleSheet(self.medical_style())
        self.current_user = None
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Instantiate pages
        self.login_page = LoginPage(self)
        self.create_user_page = CreateUserPage(self)
        self.dashboard_page = DashboardPage(self)
        self.new_test_wizard_page = NewTestWizardPage(self)
        self.results_page = ResultsPage(self)
        self.settings_page = SettingsPage(self)

        # Add pages to stack
        self.stack.addWidget(self.login_page)
        self.stack.addWidget(self.create_user_page)
        self.stack.addWidget(self.dashboard_page)
        self.stack.addWidget(self.new_test_wizard_page)
        self.stack.addWidget(self.results_page)
        self.stack.addWidget(self.settings_page)

        # Chatbot dock
        self.chatbot_dock = QDockWidget("Chatbot", self)
        self.chatbot_dock.setWidget(ChatbotWidget(self))
        self.chatbot_dock.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.addDockWidget(Qt.RightDockWidgetArea, self.chatbot_dock)

        self.show_login()

    def show_login(self):
        self.current_user = None
        self.login_page.refresh_users()
        self.stack.setCurrentWidget(self.login_page)

    def show_create_user(self):
        self.stack.setCurrentWidget(self.create_user_page)

    def show_dashboard(self):
        self.current_user = self.login_page.user_combo.currentText()
        self.dashboard_page.refresh()
        self.stack.setCurrentWidget(self.dashboard_page)

    def show_new_test(self):
        self.new_test_wizard_page.refresh()
        self.stack.setCurrentWidget(self.new_test_wizard_page)

    def show_results(self):
        self.results_page.refresh()
        self.stack.setCurrentWidget(self.results_page)

    def show_settings(self):
        self.settings_page.refresh()
        self.stack.setCurrentWidget(self.settings_page)

    def medical_style(self):
        return """
            QWidget {
                background: #f8fbff;
                font-size: 20px;
                color: #222;
            }
            QPushButton {
                background: #1976d2;
                color: white;
                border-radius: 12px;
                padding: 18px;
                font-size: 22px;
            }
            QPushButton:pressed {
                background: #1565c0;
            }
            QLineEdit, QComboBox, QCheckBox {
                font-size: 20px;
                padding: 10px;
            }
            QLabel {
                font-size: 22px;
            }
        """

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()