from email.message import EmailMessage
from win10toast import ToastNotifier
import telepot
import ssl, smtplib
from configparser import ConfigParser
import sys
from email.mime.multipart import MIMEMultipart

toast = ToastNotifier()
config = ConfigParser()
file = 'config\config.ini'
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

message = 'hello'
def send_email(message):
    port = 465  # For SSL
    password = config['email']['password']

    sender_email = config['email']['sender_email']
    receiver_email = config['email']['reciever_email']
    
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg['Subject'] = 'Device status update'
    msg['From'] = sender_email
    msg['To'] = 'wojtek.kowcz35@gmail.com'
    msg.set_content = message

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        try:
            server.login(sender_email, password)
        except smtplib.SMTPAuthenticationError:
            print("Wrong email of password")
        try:
            server.send_message(msg)
            print('success')
        except smtplib.SMTPSenderRefused:
            print("Couldn't log into email")
            toast.show_toast("Email Error", "Couldn't log into email", duration=10)
            sys.exit(1)

    # Utworzenia klienta SMTP na który zaloguje się na nasz gmail
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: # Nawiązanie bezpiecznego połączenia SSL
        # Tworzenie wiadomości
        password = config['email']['password']
        msg = MIMEMultipart() 
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = to
        body_part = MIMEText(content, 'plain') # Tworzenie treści maila
        msg.attach(body_part)

        smtp.login(sender_email, sender_password) # Logowanie do serwera

        # Jeśli mamy załącznik 
        if attatchment_name != '':
            # Załączamy załącznik 
            attatchment = MIMEApplication(open(attatchment_name, 'rb').read()) # Odczyt pliku
            attatchment.add_header("Content-Disposition", 'attachment; filename="%s"' % f'{last_name.title()} {first_name[0].upper()}.rar.txt')
            msg.attach(attatchment) 
            smtp.send_message(msg) # Wysłanie maila

send_email(message)