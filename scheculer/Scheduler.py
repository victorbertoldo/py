import schedule
import time
from roboNotepad import robo_notepad
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# def job():
#     print("I'm working...")

# schedule.every(10).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("18:56").do(robo_notepad)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

try:
    print('Iniciou!')

    schedule.every().day.at("09:36").do(robo_notepad)
    schedule.every().day.at("10:22").do(robo_notepa)

    while True:
        schedule.run_pending()
        time.sleep(1)

except IndexError as e: 
       
    # mail text
    body = f'''
                O bot notepad falhou, favor verificar.
                Erro: {e}
            '''

    # Email info
    mail_from = 'mrenginery@gmail.com'
    mail_pass = 'enginery'
    mail_to_1  = 'viktorroch@gmail.com'
    mail_to_2  = 'eu_viktor@hotmail.com'

    # Set Mime

    message = MIMEMultipart()
    message['From'] = mail_from
    message['To'] = mail_to_1
    message['To'] = mail_to_2
    message['Subject'] = 'Falha bot notepad'

    # Body message with attach content
    message.attach(MIMEText(body, 'plain'))

    # Create a SMTP session to send a mail
    session = smtplib.SMTP('smtp.gmail.com', 587) 
    session.starttls()
    session.login(mail_from, mail_pass)
    text = message.as_string()
    session.sendmail(mail_from, [mail_to_1, mail_to_2], text)
    session.quit()

else:
    print('else')