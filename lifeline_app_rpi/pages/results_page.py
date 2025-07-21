from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox
from managers.csv_manager import CsvManager
from managers.email_manager import EmailManager
from PyQt5.QtGui import QColor
import pandas as pd
import os

REFERENCE_RANGES = {
    'glucose': (70, 110),
    'iron': (60, 170),
    'b12': (200, 900),
}

class ResultsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.info_label = QLabel()
        layout.addWidget(self.info_label)
        self.table = QTableWidget()
        layout.addWidget(self.table)
        btn_layout = QHBoxLayout()
        self.save_btn = QPushButton("Save")
        btn_layout.addWidget(self.save_btn)
        self.export_btn = QPushButton("Export (CSV)")
        self.export_btn.clicked.connect(self.export_csv)
        btn_layout.addWidget(self.export_btn)
        self.email_btn = QPushButton("Email Results")
        self.email_btn.clicked.connect(self.email_results)
        btn_layout.addWidget(self.email_btn)
        self.new_test_btn = QPushButton("New Test")
        self.new_test_btn.clicked.connect(self.goto_new_test)
        btn_layout.addWidget(self.new_test_btn)
        self.back_btn = QPushButton("Back")
        self.back_btn.clicked.connect(self.goto_dashboard)
        btn_layout.addWidget(self.back_btn)
        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def refresh(self):
        user = getattr(self.parent, 'current_user', None)
        if not user:
            self.info_label.setText("No user loaded.")
            return
        tests = CsvManager.get_user_tests(user)
        if tests.empty:
            self.info_label.setText("No test results.")
            self.table.setRowCount(0)
            return
        last = tests.iloc[-1]
        self.info_label.setText(f"User: {user} | Test ID: {last['test_id']} | {last['timestamp']}")
        # Show only biomarker columns
        biomarker_cols = [c for c in tests.columns if c not in ('test_id','username','timestamp')]
        self.table.setRowCount(len(biomarker_cols)//3)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Biomarker','Value','Status'])
        for i in range(0, len(biomarker_cols), 3):
            biomarker = biomarker_cols[i]
            value = last[biomarker]
            unit = last[biomarker_cols[i+1]]
            status = last[biomarker_cols[i+2]]
            row = i//3
            self.table.setItem(row, 0, QTableWidgetItem(str(biomarker)))
            self.table.setItem(row, 1, QTableWidgetItem(f"{value} {unit}"))
            item = QTableWidgetItem(str(status))
            if status == 'low':
                item.setBackground(QColor('#ffcccc'))
            elif status == 'high':
                item.setBackground(QColor('#ffe082'))
            else:
                item.setBackground(QColor('#c8e6c9'))
            self.table.setItem(row, 2, item)
        # Hide email button if no email
        users = CsvManager.read_users()
        user_row = users[users['username'].str.lower() == user.lower()]
        email = user_row.iloc[0]['email'] if not user_row.empty else ''
        self.email_btn.setVisible(bool(email))

    def export_csv(self):
        user = getattr(self.parent, 'current_user', None)
        if not user:
            return
        tests = CsvManager.get_user_tests(user)
        path = f"{user}_results.csv"
        tests.to_csv(path, index=False)
        QMessageBox.information(self, "Exported", f"Results exported to {os.path.abspath(path)}")

    def email_results(self):
        user = getattr(self.parent, 'current_user', None)
        if not user:
            return
        users = CsvManager.read_users()
        user_row = users[users['username'].str.lower() == user.lower()]
        email = user_row.iloc[0]['email'] if not user_row.empty else ''
        if not email:
            QMessageBox.warning(self, "No Email", "No email address on file.")
            return
        tests = CsvManager.get_user_tests(user)
        path = f"{user}_results.csv"
        tests.to_csv(path, index=False)
        EmailManager.send_email(email, "Your Blood Test Results", "See attached results.", path)
        QMessageBox.information(self, "Emailed", "Results emailed!")

    def goto_new_test(self):
        self.parent.show_new_test()

    def goto_dashboard(self):
        self.parent.show_dashboard()