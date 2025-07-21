from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit

class ChatbotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Chatbot (stub)'))
        self.input = QLineEdit()
        self.input.setPlaceholderText('Type your question...')
        layout.addWidget(self.input)
        self.setLayout(layout)
