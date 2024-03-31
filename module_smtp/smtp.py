
from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path


my_email = EmailMessage()

# прописываем путь к html шаблону
html_template = Template(
    Path(r"C:\Users\md\OneDrive\python\module_smtp\templates\index.html").read_text())
html_content = html_template.safe_substitute(
    {'name': 'Maksim', 'date': 'tomorrow'})

my_email['from'] = 'Maks <maksdorozhkin@gmail.com>'
my_email['to'] = 'friend@gmail.com'
my_email['subject'] = 'Email with image'
# my_email.set_content("Yey! How are you doing?")
my_email.set_content(html_content, 'html')
# отправка изображения сначала открываем файл изображения
with open(r"C:\Users\md\OneDrive\python\module_smtp\images\2440.gif", 'rb') as img:
    image_data = img.read()
    my_email.add_attachment(image_data, maintype='image',
                            subtype='gif', filename='2440.gif')


# отправка с помощью smtplib
with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print("Email was sent!")

# сменил репозиторий
