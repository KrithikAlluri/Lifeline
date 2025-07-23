from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox, QTextEdit, QHBoxLayout, QScrollArea
from managers.csv_manager import CsvManager
from managers.encryption_manager import EncryptionManager
from utils.validation_utils import is_valid_email, is_valid_username

class CreateUserPage(QWidget):
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
        layout.addWidget(QLabel("Name:"))
        self.name_edit = QLineEdit()
        layout.addWidget(self.name_edit)
        layout.addWidget(QLabel("Password:"))
        self.pass_edit = QLineEdit()
        self.pass_edit.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.pass_edit)
        layout.addWidget(QLabel("Confirm Password:"))
        self.confirm_edit = QLineEdit()
        self.confirm_edit.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.confirm_edit)
        layout.addWidget(QLabel("Email (optional):"))
        self.email_edit = QLineEdit()
        layout.addWidget(self.email_edit)
        # Lifestyle factors
        layout.addWidget(QLabel("Age:"))
        self.age_edit = QLineEdit()
        self.age_edit.setPlaceholderText("Years")
        layout.addWidget(self.age_edit)
        layout.addWidget(QLabel("Sex:"))
        self.sex_combo = QComboBox()
        self.sex_combo.addItems(["", "Male", "Female", "Other"])
        layout.addWidget(self.sex_combo)
        layout.addWidget(QLabel("Weight (kg):"))
        self.weight_edit = QLineEdit()
        layout.addWidget(self.weight_edit)
        layout.addWidget(QLabel("Height (cm):"))
        self.height_edit = QLineEdit()
        layout.addWidget(self.height_edit)
        layout.addWidget(QLabel("Smoking:"))
        self.smoking_combo = QComboBox()
        self.smoking_combo.addItems(["", "No", "Yes"])
        layout.addWidget(self.smoking_combo)
        layout.addWidget(QLabel("Alcohol use:"))
        self.alcohol_combo = QComboBox()
        self.alcohol_combo.addItems(["", "None", "Occasional", "Regular"])
        layout.addWidget(self.alcohol_combo)
        layout.addWidget(QLabel("Exercise frequency:"))
        self.exercise_combo = QComboBox()
        self.exercise_combo.addItems(["", "None", "Some", "Regular"])
        layout.addWidget(self.exercise_combo)
        layout.addWidget(QLabel("Diet type:"))
        self.diet_combo = QComboBox()
        self.diet_combo.addItems(["", "Omnivore", "Vegetarian", "Vegan", "Other"])
        layout.addWidget(self.diet_combo)
        layout.addWidget(QLabel("Medical conditions (optional):"))
        self.conditions_edit = QTextEdit()
        self.conditions_edit.setFixedHeight(40)
        layout.addWidget(self.conditions_edit)
        layout.addWidget(QLabel("Medications (optional):"))
        self.meds_edit = QTextEdit()
        self.meds_edit.setFixedHeight(40)
        layout.addWidget(self.meds_edit)
        self.create_btn = QPushButton("Create User")
        self.create_btn.clicked.connect(self.create_user)
        layout.addWidget(self.create_btn)
        self.back_btn = QPushButton("Back")
        self.back_btn.clicked.connect(self.goto_login)
        layout.addWidget(self.back_btn)
        scroll.setWidget(form_widget)
        main_layout.addWidget(scroll)
        self.setLayout(main_layout)

    def create_user(self):
        name = self.name_edit.text().strip()
        password = self.pass_edit.text()
        confirm = self.confirm_edit.text()
        email = self.email_edit.text().strip()
        age = self.age_edit.text().strip()
        sex = self.sex_combo.currentText()
        weight = self.weight_edit.text().strip()
        height = self.height_edit.text().strip()
        smoking = self.smoking_combo.currentText()
        alcohol = self.alcohol_combo.currentText()
        exercise = self.exercise_combo.currentText()
        diet = self.diet_combo.currentText()
        conditions = self.conditions_edit.toPlainText().strip()
        meds = self.meds_edit.toPlainText().strip()
        if not is_valid_username(name):
            self.show_error("Invalid username. Use 3-32 alphanumeric characters.")
            return
        if not password or len(password) < 4:
            self.show_error("Password must be at least 4 characters.")
            return
        if password != confirm:
            self.show_error("Passwords do not match.")
            return
        if email and not is_valid_email(email):
            self.show_error("Invalid email address.")
            return
        # Age, weight, height validation (optional, skip if blank)
        if age and (not age.isdigit() or int(age) < 0 or int(age) > 120):
            self.show_error("Enter a valid age.")
            return
        if weight and (not weight.replace('.', '', 1).isdigit() or float(weight) <= 0):
            self.show_error("Enter a valid weight.")
            return
        if height and (not height.replace('.', '', 1).isdigit() or float(height) <= 0):
            self.show_error("Enter a valid height.")
            return
        try:
            CsvManager.add_user(name, EncryptionManager.hash_password(password), email,
                age, sex, weight, height, smoking, alcohol, exercise, diet, conditions, meds)
        except ValueError as e:
            self.show_error(str(e))
            return
        QMessageBox.information(self, "Success", "User created!")
        self.goto_login()

    def goto_login(self):
        self.parent.show_login()

    def show_error(self, msg):
        QMessageBox.warning(self, "Create User Failed", msg)