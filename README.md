#Desafio Técnico realizado por Bruna Bezerra.

Esse é um repositório que contêm a implementação de um robô requisitado por um desafio técnico. 
Tipo Robô: Extração de relatório

#Objetivo

#O robô criado interage com o navegador seguindo o seguinte fluxo pedido: 
Entrar no site da prefeitura do Recife >
Clicar no item "Secretaria de infraestrutura e serviços urbanos" >
Clicar no item "Área urbana" >
Clicar em "Bairros do Recife" >
Fazer o download do arquivo .CSV  >
Enviar esse arquivo para o email informado 

#Descrição 

A parte inicial do fluxo, na qual é realizado o download do arquivo, o código foi implementado usando a tecnologia Selenium em python.
Já na parte final do fluxo, no qual o robô envia o arquivo por email, o código foi feito usando algumas bibliotecas do pyhton,
entre elas a "smtplib" com o objetivo de configurar as regras de comunicação do protocolo SMTP para o envio 
do email na forma padrão. Além disso, a senha do remetente atribuída a varíável foi gerada pela própria conta da google por motivos de segurança.
Essa senha é utilizada para apenas uma ocasião que quando concluída será apagada.

OBS: Para que o robô anexasse o arquivo baixado foi necessário que eu configurasse na minha máquina o caminho padrão de download para a pasta do projeto. 

#Execução 

Para usá-lo você terá que clonar esse repositório. Após clonado, considerando que o python já está instalado no seu sistema, instale o selenium através do pip. 
Além disso, configure o caminho padrão de download da sua máquina para a pasta do projeto. Com isso, você poderá executar o projeto.




