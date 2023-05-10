<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
</head>
<body>
	<h1>Laboratório Docker</h1>
	<p>Esse é um projeto que utiliza Docker para criar três contêineres que executam diferentes aplicações:</p>
	<ul>
		<li>container-app1-site-web: um contêiner que executa um servidor web Apache com um site estático;</li>
		<li>container-app2-python: um contêiner que executa um servidor Python com uma aplicação web;</li>
		<li>container-monitoramento-nttdata: um contêiner que executa uma aplicação de monitoramento utilizando a ferramenta NTTDATA.</li>
	</ul>
	
<h2>Tecnologias utilizadas</h2>
<div>
  <a href="https://www.docker.com"><img src="https://img.icons8.com/color/48/000000/docker.png" alt="Docker" title="Docker" /></a>
  <a href="https://www.python.org"><img src="https://img.icons8.com/color/48/000000/python.png" alt="Python" title="Python" /></a>
  <a href="https://httpd.apache.org"><img src="https://img.icons8.com/color/48/000000/apache.png" alt="Apache" title="Apache" /></a>
  <a href="https://www.nttdata.com/global/en/"><img src="https://img.icons8.com/color/48/000000/ntt.png" alt="NTT DATA" title="NTT DATA" /></a>
</div>

	<br>
	<h2>Como executar o projeto</h2>
	<ol>
		<li>Clone este repositório em sua máquina local.</li>
		<li>Certifique-se de que o Docker está instalado.</li>
		<li>Abra um terminal na pasta raiz do projeto.</li>
		<li>Execute o seguinte comando para construir as imagens dos contêineres:</li>
	</ol>
	<code>docker-compose build</code>
	<ol start="5">
		<li>Execute o seguinte comando para iniciar os contêineres:</li>
	</ol>
	<code>docker-compose up</code>
	<p>Aguarde até que todos os contêineres estejam em execução.</p>
	<p>Abra um navegador web e acesse as seguintes URLs para verificar se as aplicações estão funcionando corretamente:</p>
	<ul>
		<li><a href="http://localhost:8080">http://localhost:8080</a>: o site estático do container-app1-site-web</li>
		<li><a href="http://localhost:5000">http://localhost:5000</a>: a aplicação web do container-app2-python</li>
		<li><a href="http://localhost:8081">http://localhost:8081</a>: o painel de monitoramento do container-monitoramento-nttdata</li>
	</ul>
	<h2>Como monitorar os contêineres</h2>

<p>Para monitorar os contêineres, você pode acessar o painel do container-monitoramento-nttdata, que está disponível na porta 8081. O painel apresenta informações sobre o uso de CPU, memória e rede de cada contêiner. Além disso, é possível definir alertas para serem disparados caso algum contêiner atinja um limite pré-determinado de recursos.</p>
	
<p>O container-monitoramento-nttdata também pode enviar notificações por e-mail, caso você configure as credenciais do seu servidor de e-mail no arquivo config.yml dentro da pasta container-monitoramento-nttdata.<p>

</body>
</html>
