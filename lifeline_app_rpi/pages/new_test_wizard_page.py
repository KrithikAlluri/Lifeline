from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox, QProgressBar, QMessageBox, QScrollArea
from PyQt5.QtCore import QTimer
from managers.csv_manager import CsvManager
import datetime
import random

BIOMARKERS = [
    ("glucose", "mg/dL"),
    ("iron", "ug/dL"),
    ("b12", "pg/mL"),
    ("cholesterol", "mg/dL"),
    ("triglycerides", "mg/dL"),
    ("calcium", "mg/dL"),
    ("vitamin D", "ng/mL"),
    ("potassium", "mmol/L"),
    ("sodium", "mmol/L"),
    ("magnesium", "mg/dL"),
    ("zinc", "ug/dL"),
]

class NewTestWizardPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        form_widget = QWidget()
        layout = QVBoxLayout(form_widget)
        self.user_label = QLabel()
        layout.addWidget(self.user_label)
        layout.addWidget(QLabel("Select up to 10 biomarkers:"))
        self.checkboxes = []
        for biomarker, _ in BIOMARKERS:
            cb = QCheckBox(biomarker)
            self.checkboxes.append(cb)
            layout.addWidget(cb)
        self.start_btn = QPushButton("Start Test")
        self.start_btn.clicked.connect(self.start_test)
        layout.addWidget(self.start_btn)
        self.progress = QProgressBar()
        self.progress.setValue(0)
        layout.addWidget(self.progress)
        scroll.setWidget(form_widget)
        main_layout.addWidget(scroll)
        self.setLayout(main_layout)

    def refresh(self):
        user = getattr(self.parent, 'current_user', None)
        self.user_label.setText(f"User: {user}")
        for cb in self.checkboxes:
            cb.setChecked(False)
        self.progress.setValue(0)

    def start_test(self):
        selected = [cb.text() for cb in self.checkboxes if cb.isChecked()]
        if not selected or len(selected) > 10:
            QMessageBox.warning(self, "Error", "Select 1-10 biomarkers.")
            return
        self.progress.setValue(0)
        self.start_btn.setEnabled(False)
        self.simulate_test(selected)

    def simulate_test(self, biomarkers):
        self.progress.setValue(0)
        self._progress = 0
        self._biomarkers = biomarkers
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._advance_progress)
        self._timer.start(200)

    def _advance_progress(self):
        self._progress += 10
        self.progress.setValue(self._progress)
        if self._progress >= 100:
            self._timer.stop()
            self.save_test()
            self.start_btn.setEnabled(True)

    def save_test(self):
        user = getattr(self.parent, 'current_user', None)
        if not user:
            return
        test_id = int(datetime.datetime.now().timestamp())
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        row = {
            'test_id': test_id,
            'username': user,
            'timestamp': timestamp,
        }
        for biomarker, unit in BIOMARKERS:
            if biomarker in self._biomarkers:
                value = random.randint(80, 120)
                status = 'normal'
                row[f'{biomarker}'] = value
                row[f'{biomarker}_unit'] = unit
                row[f'{biomarker}_status'] = status
        CsvManager.add_test(row)
        QMessageBox.information(self, "Test Complete", "Test results saved.")
        self.parent.show_results()