import pyautogui as ui
import rpa as r
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pandas import Timestamp

r.init()
r.url('https://www.melhorcambio.com/dolar-hoje')
ui.sleep(5)
window = ui.getActiveWindow()
window.maximize()
dolar_comercial = r.read('//*[@id="comercial"]')
r.close()

# mail text
body = 'Cotação hoje(' + str(Timestamp('today')) + '): ' + dolar_comercial

# Email info
mail_from = 'mrenginery@gmail.com'
mail_pass = 'enginery'
mail_to  = 'viktorroch@gmail.com'

# Set Mime

message = MIMEMultipart()
message['From'] = mail_from
message['To'] = mail_to
message['Subject'] = 'Cotação do dolar'

# Body message with attach content
message.attach(MIMEText(body, 'plain'))

# Create a SMTP session to send a mail
session = smtplib.SMTP('smtp.gmail.com', 587) 
session.starttls()
session.login(mail_from, mail_pass)
text = message.as_string()
session.sendmail(mail_from, mail_to, text)
session.quit()
