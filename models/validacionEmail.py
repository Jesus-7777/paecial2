from smtplib import SMTP
from email.message import EmailMessage
from config import settings


def envioEmail(nombre,correo,token):
    message = EmailMessage()
    message['Subject'] = 'Hola '+nombre+', verifica tu cuenta ahora mismo.'
    message['From'] = 'jesusnarvaez2020@itp.edu.co'
    message['To'] = correo
    message.set_content(" <center><img src="'https://upload.wikimedia.org/wikipedia/commons/8/83/Logo_tuenti_positivo_color.png '" 'height="'50%'" width="'50%'"' </center>\n\n <h1> Te damos la bienvenido a muestro Portal </h1>\n\n  <h3> Para verificar tu cuenta, solamente debes hacer clic en <a href='http://localhost:5000/valida_email/{}'> Activar mi cuenta </a> y del resto ya nos encargaremos nosotros. ¡Adiós! </h3> ".format(token),subtype='html')

    username = settings.SMPT_USERNAME
    password = settings.SMPT_PASSWORD
    """ print(username,password,settings.SMPT_HOSTNAME) """
    server=SMTP(settings.SMPT_HOSTNAME)
    server.starttls()
    server.login(username, password)
    server.send_message(message)
    server.quit()

def sendPassReset(correo,token):
    message = EmailMessage()
    message['Subject'] = 'Hola, restablece tu contraseñ.'
    message['From'] = 'jesusnarvaez2020@itp.edu.co'
    message['To'] = correo
    message.set_content(" <center><img src="'https://upload.wikimedia.org/wikipedia/commons/8/83/Logo_tuenti_positivo_color.png '" 'height="'50%'" width="'50%'"' </center>\n\n <h1> Te damos la bienvenido a muestro Portal </h1>\n\n  <h3> Para el cambio de contraseña, solamente debes hacer clic en <a href='http://localhost:5000/reset/{}'> Restablecer contraseña </a> y del resto ya nos encargaremos nosotros. ¡Adiós! </h3> ".format(token),subtype='html')

    username = settings.SMPT_USERNAME
    password = settings.SMPT_PASSWORD
    """ print(username,password,settings.SMPT_HOSTNAME) """
    server=SMTP(settings.SMPT_HOSTNAME)
    server.starttls()
    server.login(username, password)
    server.send_message(message)
    server.quit()