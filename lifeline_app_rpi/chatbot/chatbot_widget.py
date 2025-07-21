from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class ChatbotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel("Chatbot (stub):")
        layout.addWidget(self.label)
        self.input = QLineEdit()
        layout.addWidget(self.input)
        self.send_btn = QPushButton("Send")
        self.send_btn.clicked.connect(self.echo)
        layout.addWidget(self.send_btn)
        self.setLayout(layout)

    def echo(self):
        text = self.input.text()
        self.label.setText(f"You said: {text}")
        self.input.clear()