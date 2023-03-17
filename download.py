from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#para anexar arquivo no email
from email.mime.base import MIMEBase
from email import encoders

#abrir navegador
aba_prefeitura = webdriver.Chrome()
aba_prefeitura.maximize_window() 
#entrar no site requisitado
aba_prefeitura.get('http://dados.recife.pe.gov.br/organization')
time.sleep(2)

#seguir um fluxo/caminho definido de encontrar o elemento pelo xpath e clicar nele até fazer o download do arquivo
elemento1 = aba_prefeitura.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/article/div/ul/li[19]/a').click()
time.sleep(2)
elemento2 = aba_prefeitura.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/article/div/ul/li[1]/div/h3/a').click()
time.sleep(2)
elemento3 = aba_prefeitura.find_element(By.XPATH, '//*[@id="dataset-resources"]/ul/li[1]/div/a').click()
time.sleep(2)
elemento4 = aba_prefeitura.find_element(By.XPATH, '//*[@id="dataset-resources"]/ul/li[1]/div/ul/li[2]/a').click()
time.sleep(2)
aba_prefeitura.close()

#fluxo final do arquivo sendo enviado por email
#concectar com servidor SMTP
#dados de host e porta disponibiliado pelo proprio gmail
host = "smtp.gmail.com"
porta = "587"
login = "brubslubs2019@gmail.com" #email criado para desafio
senha = "iwdzoexhzszyvpcb" #senha gerada pelo google para apenas um uso

#instanciando a conexão com servidor
server = smtplib.SMTP(host,porta)

#o gmail pede que a segurança também seja ativada com o TLS
server.ehlo()
server.starttls()

#fazer o login
server.login(login, senha)

#construção do email
corpo = "Envio automatizado do arquivo baixado pelo robô implementado pela candidata Bruna Bezerra Ferreira de Caravalho. Segue o link do repositório:  "

#dando o formato mime ao meu email para preencher
email_msg = MIMEMultipart()

email_msg['From'] = login #meu email já declarado
email_msg['To'] = login #teste
email_msg['Subject'] = "ENTREGA DO DESAFIO VAGA ESTÁGIO TI | PROCESSO SELETIVO QCA" #assunto

#caminho do arquivo que será anexado
caminho = "C:/Users/magalu/Desktop/Desafio_selenium/bairro.csv"
arquivo = open(caminho,'rb') #lendo binario do arquivo que esta no caminho e guardando nessa variavel

#com o binário transformar em base 64 para enviar
#anexo do tipo mimebase
anexo = MIMEBase('application', 'octet-stream') #usar o mimebase importado para criar o anexo
anexo.set_payload(arquivo.read())
encoders.encode_base64(anexo)

#adicionar header para definir o nome do arquivo que vai estar no email
anexo.add_header('Content-Disposition', f'anexado; filename= bairro.csv') #conteudo do arquivo é um anexo que tem nome bairro
arquivo.close()
email_msg.attach(anexo) #anexando de fato o arquivo no corpo no meu email

#anexar o email preenchido no texto com formato mime e tipo plain
email_msg.attach(MIMEText(corpo,'plain'))

#enviar (de quem, para quem, msg)
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
server.quit()
