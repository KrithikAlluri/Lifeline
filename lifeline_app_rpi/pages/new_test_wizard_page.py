from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox, QProgressBar, QMessageBox, QScrollArea
from PyQt5.QtCore import QTimer
from managers.csv_manager import CsvManager
import datetime
import random

# Reference ranges for biomarker interpretation
REFERENCE_RANGES = {
    'glucose': (70, 110),
    'creatinine': (0.6, 1.2),
    'urea': (7, 20),
    'potassium': (3.5, 5.0),
    'albumin': (3.4, 5.4),
    'hemoglobin': (12, 16),
    'uric_acid': (3.4, 7.0),
    'vitamin_b12': (200, 900),
}

BIOMARKERS = [
    ("glucose", "mg/dL"),
    ("creatinine", "mg/dL"),
    ("urea", "mg/dL"),
    ("potassium", "mmol/L"),
    ("albumin", "g/dL"),
    ("hemoglobin", "g/dL"),
    ("uric_acid", "mg/dL"),
    ("vitamin_b12", "pg/mL"),
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
                # Generate realistic values for each biomarker
                if biomarker == 'glucose':
                    value = random.uniform(70, 110)
                elif biomarker == 'creatinine':
                    value = random.uniform(0.6, 1.2)
                elif biomarker == 'urea':
                    value = random.uniform(7, 20)
                elif biomarker == 'potassium':
                    value = random.uniform(3.5, 5.0)
                elif biomarker == 'albumin':
                    value = random.uniform(3.4, 5.4)
                elif biomarker == 'hemoglobin':
                    value = random.uniform(12, 16)
                elif biomarker == 'uric_acid':
                    value = random.uniform(3.4, 7.0)
                elif biomarker == 'vitamin_b12':
                    value = random.uniform(200, 900)
                else:
                    value = random.uniform(80, 120)
                
                # Determine status based on reference ranges
                if biomarker in REFERENCE_RANGES:
                    min_val, max_val = REFERENCE_RANGES[biomarker]
                    if value < min_val:
                        status = 'low'
                    elif value > max_val:
                        status = 'high'
                    else:
                        status = 'normal'
                else:
                    status = 'normal'
                
                row[f'{biomarker}'] = round(value, 2)
                row[f'{biomarker}_unit'] = unit
                row[f'{biomarker}_status'] = status
        CsvManager.add_test(row)
        QMessageBox.information(self, "Test Complete", "Test results saved.")
        self.parent.show_results()