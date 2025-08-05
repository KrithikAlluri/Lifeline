import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class EmailManager:
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
    SMTP_USER = os.getenv('SMTP_USER', '')
    SMTP_PASS = os.getenv('SMTP_PASS', '')

    @staticmethod
    def send_email(to_email, subject, body, attachment_path=None):
        # Check if email is configured
        if not EmailManager.SMTP_USER or not EmailManager.SMTP_PASS:
            print(f"[EMAIL NOT CONFIGURED] Would send to {to_email}\nSubject: {subject}\nBody: {body}\nAttachment: {attachment_path}")
            return True
            
        try:
            msg = MIMEMultipart()
            msg['From'] = EmailManager.SMTP_USER
            msg['To'] = to_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            if attachment_path:
                with open(attachment_path, "rb") as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename= {attachment_path}')
                msg.attach(part)
            
            server = smtplib.SMTP(EmailManager.SMTP_SERVER, EmailManager.SMTP_PORT)
            server.starttls()
            server.login(EmailManager.SMTP_USER, EmailManager.SMTP_PASS)
            text = msg.as_string()
            server.sendmail(EmailManager.SMTP_USER, to_email, text)
            server.quit()
            return True
        except Exception as e:
            print(f"Email error: {e}")
            return False