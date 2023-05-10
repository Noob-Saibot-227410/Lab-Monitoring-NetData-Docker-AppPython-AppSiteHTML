# Define a imagem base
FROM nginx:1.19.10-alpine

# Copia os arquivos de configuração para o contêiner
COPY app1 /usr/share/nginx/html

# Expõe a porta 80 do contêiner
EXPOSE 80

# Define o comando a ser executado ao iniciar o contêiner
CMD ["nginx", "-g", "daemon off;"]
