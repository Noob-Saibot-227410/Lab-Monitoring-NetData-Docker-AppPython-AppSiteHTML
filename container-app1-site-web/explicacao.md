app1, que contém um site web básico:

---

Explicação das linhas do Dockerfile:

FROM nginx:1.19.10-alpine: define a imagem base a ser usada para o contêiner. Neste caso, estamos usando a imagem do Nginx na versão 1.19.10, que é baseada no Alpine Linux, uma distribuição Linux leve.

COPY app1 /usr/share/nginx/html: copia o conteúdo do diretório app1 do host para o diretório /usr/share/nginx/html do contêiner. O diretório app1 contém os arquivos HTML, CSS e JavaScript que serão servidos pelo Nginx.

EXPOSE 80: expõe a porta 80 do contêiner, que é a porta padrão do Nginx.

CMD ["nginx", "-g", "daemon off;"]: define o comando a ser executado quando o contêiner é iniciado. Neste caso, estamos executando o Nginx e definindo o parâmetro -g daemon off; para que o Nginx não rode em modo daemon, permitindo que o Docker gerencie o processo.

---

O diretório app1 é o diretório de trabalho do contêiner container-app1-site-web, que contém os arquivos necessários para executar o site web. O index.html é a página principal do site, que será exibida quando o site for acessado pelo navegador. O arquivo style.css contém a folha de estilo que será aplicada ao site e o script.js é um arquivo de script JavaScript que contém a lógica de interação do site.