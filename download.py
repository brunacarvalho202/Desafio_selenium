from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#abrir navegador
aba_prefeitura = webdriver.Chrome()
aba_prefeitura.maximize_window() 
#entrar no site requisitado
aba_prefeitura.get('http://dados.recife.pe.gov.br/organization')
time.sleep(3)

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
