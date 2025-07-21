# Lifeline Blood Testing Kit App (Raspberry Pi 4)

A modular, touchscreen-friendly PyQt5 app for the Lifeline $50 blood testing kit, designed for Raspberry Pi 4 (2GB RAM, 5” touchscreen). All user and test data is stored in CSV files with password hashes. Supports multi-user login, optional email, test history, and a chatbot.

## Features
- Multi-user login with password hashing
- Create users with optional email
- Per-user dashboard and test history
- New test wizard (mock data)
- Results with export/email
- Touchscreen-optimized UI
- Chatbot panel
- All data in CSV (no SQL)

## Directory Structure
```
lifeline_app_rpi/
    main.py
    requirements.txt
    assets/
    data/
        users.csv
        tests.csv
    pages/
        login_page.py
        create_user_page.py
        dashboard_page.py
        new_test_wizard_page.py
        results_page.py
        settings_page.py
    managers/
        csv_manager.py
        email_manager.py
        encryption_manager.py
    chatbot/
        chatbot_widget.py
    utils/
        validation_utils.py
```

## Setup Instructions

1. **Install dependencies:**
   ```bash
   sudo apt update
   sudo apt install python3-pyqt5 python3-pip
   pip3 install -r requirements.txt
   ```
2. **Run the app:**
   ```bash
   python3 main.py
   ```
3. **Touchscreen:**
   - Optimized for 5” Raspberry Pi touchscreen.
   - Large buttons, medical-style UI.

## Data Files
- `data/users.csv`: Stores users (username, password hash, email)
- `data/tests.csv`: Stores test results

## Email Setup
- Configure SMTP in `managers/email_manager.py` (supports Gmail app password or local server)

## Notes
- All data is stored in CSV for easy backup and transfer.
- Passwords are hashed (SHA-256).
- No plain text passwords are stored.

## Demo Users
See `data/users.csv` for example users.

---

MIT License