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
from pages.chatbot_page import ChatbotPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lifeline Blood Testing Kit")
        # 5x2.5 inch at 160 DPI, portrait = 400x800 px
        self.setMinimumSize(400, 800)
        self.setFixedSize(400, 800)
        # self.setBaseSize(400, 800)
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
        self.chatbot_page = ChatbotPage(self)

        # Add pages to stack
        self.stack.addWidget(self.login_page)
        self.stack.addWidget(self.create_user_page)
        self.stack.addWidget(self.dashboard_page)
        self.stack.addWidget(self.new_test_wizard_page)
        self.stack.addWidget(self.results_page)
        self.stack.addWidget(self.settings_page)
        self.stack.addWidget(self.chatbot_page)

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
        self.dashboard_page.set_chatbot_button_visible(True)

    def show_new_test(self):
        self.new_test_wizard_page.refresh()
        self.stack.setCurrentWidget(self.new_test_wizard_page)

    def show_results(self):
        self.results_page.refresh()
        self.stack.setCurrentWidget(self.results_page)

    def show_settings(self):
        self.settings_page.refresh()
        self.stack.setCurrentWidget(self.settings_page)

    def show_chatbot(self):
        self.chatbot_page.open_chatbot()
        self.stack.setCurrentWidget(self.chatbot_page)

    def toggle_chatbot(self):
        if self.chatbot_dock.isVisible():
            self.chatbot_dock.hide()
        else:
            self.chatbot_dock.show()

    def medical_style(self):
        return """
            QWidget {
                background: #fafdff;
                font-size: 22px;
                color: #1a237e;
            }
            QPushButton {
                background: #1976d2;
                color: white;
                border-radius: 14px;
                padding: 10px 0px;
                font-size: 20px;
                margin: 6px 0px;
                min-height: 40px;
            }
            QPushButton:pressed {
                background: #1565c0;
            }
            QLineEdit, QComboBox, QCheckBox {
                font-size: 20px;
                padding: 12px;
                border-radius: 8px;
                border: 1px solid #b0bec5;
                margin-bottom: 10px;
            }
            QLabel {
                font-size: 22px;
                margin-bottom: 6px;
            }
            QTableWidget {
                font-size: 18px;
                background: #ffffff;
                border-radius: 8px;
            }
            QHeaderView::section {
                background: #e3f2fd;
                font-size: 18px;
                border-radius: 6px;
            }
        """

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()