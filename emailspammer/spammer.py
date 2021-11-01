import os
import smtplib
from email.message import EmailMessage


def send_email(email_address, email_password, to_email_address, subject, *body):
    try:
        final_send_message = ""
        for sentence_ig in body:
            final_send_message += f""" {sentence_ig}"""
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        try:
            server.login(email_address, email_password)
        except Exception as e:
            print("- Error: Unable to login.", e)
        email = EmailMessage()

        email['From'] = email_address
        email['To'] = to_email_address
        email['Subject'] = subject
        email.set_content(final_send_message)
        server.send_message(email)
        server.close()

    except Exception as e:
        print("- Error: Unable to send email", e)
        return


