FROM python:3.11

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /microservice_user

# Copie o arquivo requirements.txt para o contêiner
COPY requeriments.txt .

# Instale as dependências da aplicação
RUN pip install -r requeriments.txt

# Copie o restante dos arquivos da aplicação para o contêiner
COPY . .

# Comando a ser executado quando o contêiner for iniciado
CMD ["python", "run.py"]