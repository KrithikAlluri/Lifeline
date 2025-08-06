import json
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from managers.csv_manager import CsvManager
import sys
import os

# Import the model manager
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_manager import local_gemma_inference

USER_AVATAR = "🧑"
BOT_AVATAR = "🩸"  # or use "🤖" for a robot look
BOT_NAME = "Lifeline"

class ChatInput(QTextEdit):
    def __init__(self, send_callback, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.send_callback = send_callback
        self.setFixedHeight(40)
        self.setStyleSheet("font-size: 16px;")

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            if event.modifiers() & Qt.ShiftModifier:
                super().keyPressEvent(event)
            else:
                self.send_callback()
                event.accept()
        else:
            super().keyPressEvent(event)

class ChatbotPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.messages = []
        self.init_ui()

    def open_chatbot(self):
        self.messages = []
        self.add_preprompt()
        self.chat_history.clear()
        self.input.setDisabled(True)
        self.send_btn.setDisabled(True)
        self.get_first_bot_message()

    def add_preprompt(self):
        preprompt = ("")
#     """You are Lifeline, a friendly and knowledgeable assistant built into a blood-testing app. Your role is to:
# 1. Interpret numeric biomarker results (e.g., glucose, iron) using standard medical reference ranges.
# 2. Provide a clear explanation in plain language, but dont talk too much.
# 3. Use calm, supportive tone, without bold or Markdown and dont use emojis.
# 4. If you don’t have enough information, ask clarifying questions.

# Example conversation:

# User: My glucose is 65 mg/dL. Is that low?
# Lifeline: A glucose of 65 mg/dL is slightly below the typical fasting range (70–99 mg/dL). That’s considered mild hypoglycemia but not severe. You might feel shaky or tired. Make sure to have a balanced snack soon and monitor how you feel. This is educational only—please consult your doctor.

# User: What does CRP at 10 mg/L mean?
# Lifeline: A CRP of 10 mg/L indicates moderate inflammation. Normal CRP is below 5 mg/L, so this suggests your body might be responding to an infection or stress. If you have symptoms or persistent elevation, talk to your doctor. This is educational only—please consult your doctor.

# Now respond as Lifeline. If the user refers to any blood test results, look at their blood tests below: """
# )
        # Add past blood tests if user is logged in
        user = getattr(self.parent, 'current_user', None)
        if user:
            try:
                tests = CsvManager.get_user_tests(user)
                if not tests.empty:
                    preprompt += "\nHere are the patient's last blood tests:"
                    for _, row in tests.tail(10).iterrows():
                        summary = f"\nTest on {row['timestamp']}: "
                        for col in tests.columns:
                            if col not in ('test_id','username','timestamp') and str(row[col]) != '' and not col.endswith('_unit') and not col.endswith('_status'):
                                val = row[col]
                                unit = row.get(f'{col}_unit', '')
                                status = row.get(f'{col}_status', '')
                                summary += f"{col}: {val} {unit} ({status}), "
                        preprompt += summary.rstrip(', ')
            except Exception as e:
                preprompt += f"\n[Could not load test history: {e}]"
            
        preprompt += "\nStart off by saying Hi! and then ask the user( by their name) what they want to know."
        self.messages.append({"role": "user", "content": preprompt})
        # print(preprompt)
    def init_ui(self):
        main_layout = QVBoxLayout()
        # Top bar with dashboard button
        top_bar = QHBoxLayout()
        top_bar.addStretch()
        self.home_btn = QPushButton("Go to Dashboard")
        self.home_btn.setFixedWidth(180)
        self.home_btn.clicked.connect(self.goto_dashboard)
        top_bar.addWidget(self.home_btn)
        main_layout.addLayout(top_bar)
        # Chat area
        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)
        self.chat_history.setStyleSheet("background: #fff; color: #111; font-size: 18px;")
        self.chat_history.setMinimumHeight(300)
        main_layout.addWidget(self.chat_history)
        # Input area
        input_layout = QHBoxLayout()
        self.input = ChatInput(self.send_message)
        input_layout.addWidget(self.input)
        self.send_btn = QPushButton("Send")
        self.send_btn.setFixedWidth(120)
        self.send_btn.clicked.connect(self.send_message)
        input_layout.addWidget(self.send_btn)
        main_layout.addLayout(input_layout)
        self.setLayout(main_layout)

    def send_message(self):
        user_msg = self.input.toPlainText().strip()
        if not user_msg:
            return
        self.append_message("You", user_msg, USER_AVATAR)
        self.input.clear()
        self.messages.append({"role": "user", "content": user_msg})
        self.get_bot_response()

    def append_message(self, sender, message, avatar):
        self.chat_history.append(f"<b>{avatar} {sender}:</b> {message}")

    def get_bot_response(self):
        self.append_message(BOT_NAME, f"<i>{BOT_NAME} is typing...</i>", BOT_AVATAR)
        self.typing_line = True
        try:
            # Use local inference instead of API call
            bot_reply = local_gemma_inference(self.messages)
            self.remove_typing_line()
            self.append_message(BOT_NAME, bot_reply, BOT_AVATAR)
            self.messages.append({"role": "assistant", "content": bot_reply})
        except Exception as e:
            self.remove_typing_line()
            self.append_message(BOT_NAME, f"[Error: {str(e)}]", BOT_AVATAR)

    def remove_typing_line(self):
        text = self.chat_history.toHtml().strip().split("<br>")
        if len(text) > 1:
            text = text[:-1]
        self.chat_history.setHtml("<br>".join(text))

    def get_first_bot_message(self):
        self.append_message(BOT_NAME, f"<i>{BOT_NAME} is typing...</i>", BOT_AVATAR)
        try:
            # Use local inference instead of API call
            bot_reply = local_gemma_inference(self.messages)
            self.remove_typing_line()
            self.append_message(BOT_NAME, bot_reply, BOT_AVATAR)
            self.messages.append({"role": "assistant", "content": bot_reply})
        except Exception as e:
            self.remove_typing_line()
            self.append_message(BOT_NAME, f"[Error: {str(e)}]", BOT_AVATAR)
        self.input.setDisabled(False)
        self.send_btn.setDisabled(False)

    def goto_dashboard(self):
        self.parent.show_dashboard() 