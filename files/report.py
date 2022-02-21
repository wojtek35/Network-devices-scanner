from win10toast import ToastNotifier
import winsound
import telepot
import ssl, smtplib
from configparser import ConfigParser
import os
import sys

toast = ToastNotifier()
config = ConfigParser()
file = 'config.ini'
config.read(file)

def send_telegram(info):
    api_id = '19334622'
    api_hash = 'e81856e5a897ecaf03e32a551395688a'

    token = config['Bot info']['token'] # telegram token
    receiver_id = config['Bot info']['chat_id'] # https://api.telegram.org/bot<TOKEN>/getUpdates

    message = """\
    Subject: Device status update

    """
    message += info
    bot = telepot.Bot(token)

    bot.sendMessage(receiver_id, message) # send a activation message to telegram receiver id

def send_email(info):
    port = 465  # For SSL
    password = config['email']['password']

    sender_email = config['email']['sender_email']
    receiver_email = config['email']['reciever_email']
    message = """\
    Subject: Device status update

    """
    message += info
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        try:
            server.login(sender_email, password)
        except smtplib.SMTPAuthenticationError:
            print("Wrong email of password")
        try:
            server.sendmail(sender_email, receiver_email, message)
        except smtplib.SMTPSenderRefused:
            print("Couldn't log into email")
            toast.show_toast("Email Error", "Couldn't log into email", duration=10)
            sys.exit(1)