from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox, QProgressBar

class NewTestWizardPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.addWidget(QLabel('New Test Wizard'))
        self.user_label = QLabel('User:')
        layout.addWidget(self.user_label)
        self.biomarker_checks = []
        for i in range(10):
            cb = QCheckBox(f'Biomarker {i+1}')
            layout.addWidget(cb)
            self.biomarker_checks.append(cb)
        self.start_test_button = QPushButton('Start Test')
        layout.addWidget(self.start_test_button)
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)
