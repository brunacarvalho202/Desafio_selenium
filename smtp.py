import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.base import MIMEBase

#concectar com servidor SMTP
#dados de host e porta disponibiliado pelo proprio gmail
host = "smtp.gmail.com"
porta = "587"
login = "brubslubs2019@gmail.com"
senha = "iwdzoexhzszyvpcb" #senha gerada pelo google para apenas um uso

#instanciando a conexão com servidor
server = smtplib.SMTP(host,porta)

#o gmail pede que a segurança também seja ativada com o TLS
server.ehlo()
server.starttls()

#fazer o login
server.login(login,senha)

#construção do email
corpo = "conteudo do email para teste"

#dando o formato mime ao meu email para preencher
email_msg = MIMEMultipart()

email_msg['From'] = login #meu email já declarado
email_msg['To'] = "cleison.carvalho2018@gmail.com" #teste
email_msg['Subject'] = "teste de email automatizado" #assunto

#anexar o email preenchido no texto com formato mime e tipo plain
email_msg.attach(MIMEText(corpo,'plain'))

#enviar (de quem, para quem, msg)
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
server.quit()