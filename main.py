import smtplib
from email.message import EmailMessage
import schedule
import time

def mail_gonder():
    gonderen = """ 'mailiniz' """
    sifre = """ '16karakterliksifreniz' """
    alici_listesi = [
        'mail1@gmail.com',
        'mail2@gmail.com',
        'mail3@gmail.com',
        'mail4@gmail.com'
    ]
    konu = ' '
    icerik = ' '

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(gonderen, sifre)

        for index, alici in enumerate(alici_listesi, start=1):
            msg = EmailMessage()
            msg['Subject'] = konu
            msg['From'] = gonderen
            msg['To'] = alici
            msg.set_content(icerik)

            smtp.send_message(msg)
            print( f"{index}. Mail gönderildi: {alici}")


# Çalıştırınca listedekilere tek tek mail gitsin
mail_gonder()