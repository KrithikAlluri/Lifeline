class EmailManager:
    """
    Stub for sending emails. Replace with real SMTP logic as needed.
    """
    @staticmethod
    def send_email(to_email, subject, body, attachment_path=None):
        print(f"[Email Stub] To: {to_email}, Subject: {subject}, Attachment: {attachment_path}")
        print(f"Body:\n{body}")
        return True
