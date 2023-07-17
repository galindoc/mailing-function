import os, smtplib, ssl, json

from dotenv import load_dotenv


load_dotenv()

email_sender = os.getenv("EMAIL_SENDER")
email_password = os.getenv("EMAIL_PASSWORD")
email_receiver = "christian.galindo95@outlook.com"

def send_verification_email(email_receiver, token):
    print(email_sender, email_password)
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = email_sender  # Enter your address
    receiver_email = email_receiver  # Enter receiver address
    password = email_password
    message = """\
    Subject: Email Verification

    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

send_verification_email(email_receiver, "token")
