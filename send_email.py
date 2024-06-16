import smtplib, ssl
import os


# Simple Mail Transfer Protocol (SMTP)
# SSL/TLS (Secure Sockets Layer/Transport Layer Security).

def my_send_email(message):
    message=f"""\
    subject: event\n
    {message}

"""
    host = "smtp.gmail.com"
    port = 465
    username = os.getenv("Gmail")
    password = os.getenv("PASSWORD")

    receiver = os.getenv("Gmail")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

