# Define a imagem base
FROM python:3.9

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app2

# Copia o arquivo requirements.txt para dentro do contêiner
COPY ./app2/requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo da pasta app2 para dentro do contêiner
COPY ./app2 .

# Expõe a porta 5000 do contêiner para o host
EXPOSE 5000

# Comando para executar a aplicação
CMD ["python", "main.py"]
