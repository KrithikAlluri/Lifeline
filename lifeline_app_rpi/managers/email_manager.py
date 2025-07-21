class EmailManager:
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    SMTP_USER = ''  # Set in config
    SMTP_PASS = ''  # Set in config

    @staticmethod
    def send_email(to_email, subject, body, attachment_path=None):
        # For MVP, just print. Replace with real SMTP logic for production.
        print(f"Sending email to {to_email}\nSubject: {subject}\nBody: {body}\nAttachment: {attachment_path}")
        return True