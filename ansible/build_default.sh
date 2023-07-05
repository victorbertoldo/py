#!/bin/bash

# Nome do arquivo de log
log_file="script.log"

# Função para registrar mensagens de log
log_message() {
  echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" >> "$log_file"
}

# Verifica se o subdomínio foi fornecido como argumento
if [ $# -eq 0 ]; then
  log_message "ERRO: Você precisa fornecer o valor do subdomínio como argumento."
  exit 1
fi

# Atribui o valor do subdomínio ao subdominiodocliente
subdominiodocliente="$1"

# Configurações iniciais
log_message "Iniciando configurações iniciais..."

# Instalação do Vim
log_message "Instalando o Vim..."
sudo apt-get install -y vim

if [ $? -eq 0 ]; then
  log_message "Instalação do Vim concluída com sucesso."
else
  log_message "ERRO: Falha na instalação do Vim."
fi

# Configuração do timezone
log_message "Configurando o timezone..."
sudo timedatectl set-timezone America/Sao_Paulo

if [ $? -eq 0 ]; then
  log_message "Configuração do timezone concluída com sucesso."
else
  log_message "ERRO: Falha na configuração do timezone."
fi

# Alteração da porta SSH
log_message "Alterando a porta SSH..."
sudo sed -i 's/Port 22/Port 1584/' /etc/ssh/sshd_config
sudo service sshd restart

if [ $? -eq 0 ]; then
  log_message "Alteração da porta SSH concluída com sucesso."
else
  log_message "ERRO: Falha na alteração da porta SSH."
fi

if [ $? -eq 0 ]; then
  log_message "Configuração do inicial concluída com sucesso."
else
  log_message "ERRO: Falha na configuração inicial."
fi

# Atualização do apt
log_message "Atualizando o apt..."
sudo apt-get update
sudo apt-get upgrade -y

if [ $? -eq 0 ]; then
  log_message "Atualização do apt concluida."
else
  log_message "ERRO: Falha na Atualização do apt."
fi

# Instalação do Java 11
log_message "Iniciando a instalação e configuração do java..."
sudo apt install openjdk-11-jdk -y

# Configuração da variável de ambiente do Java
sudo update-alternatives --config java
JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64/bin/java"
echo "JAVA_HOME=\"/usr/lib/jvm/java-11-openjdk-amd64/bin/java\"" | sudo tee -a /etc/environment
source /etc/environment

if [ $? -eq 0 ]; then
  log_message "Instalação e configuração do java concluida."
else
  log_message "ERRO: Falha na instalação e configuração do java."
fi

# Instalação do Metabase
log_message "Iniciando a configuração inicial do Metabase..."
sudo mkdir /opt/metabase
sudo addgroup metabase
sudo adduser --system --ingroup metabase --disabled-login metabase
sudo chown -R metabase:metabase /opt/metabase/
sudo touch /var/log/metabase.log
sudo chown syslog:adm /var/log/metabase.log
sudo touch /etc/default/metabase
sudo chmod 640 /etc/default/metabase
sudo touch /etc/systemd/system/metabase.service
sudo touch /etc/rsyslog.d/metabase.conf

if [ $? -eq 0 ]; then
  log_message "Instalação e configuração inicial do Metabase concluida."
else
  log_message "ERRO: Falha na configuração inicial do Metabase."
fi

log_message "Iniciando o download do Metabase..."
cd /opt/metabase
sudo wget https://downloads.metabase.com/v0.44.5/metabase.jar
sudo chmod +x /opt/metabase/metabase.jar

if [ $? -eq 0 ]; then
  log_message "Download do Metabase concluido."
else
  log_message "ERRO: Falha no download do Metabase."
fi

log_message "Iniciando a configuração do Metabase como serviço..."
sudo tee /etc/systemd/system/metabase.service > /dev/null <<EOT
[Unit]
Description=Metabase
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/bin/java -jar /opt/metabase/metabase.jar
WorkingDirectory=/opt/metabase
User=metabase
Type=simple
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOT


if [ $? -eq 0 ]; then
  log_message "Configuração do Metabase como serviço concluido."
else
  log_message "ERRO: Falha na Configuração do Metabase como serviço."
fi

log_message "Habilitando e iniciando o serviço do Metabase..."
sudo systemctl enable metabase
sudo systemctl start metabase

if [ $? -eq 0 ]; then
  log_message "Habilitação e inicialização do serviço do Metabase concluido."
else
  log_message "ERRO: Falha na Habilitação e inicialização do serviço do Metabase."
fi

# Instalação do Nginx
log_message "Iniciando a instalação e configuração do NGINX ..."
sudo apt-get install nginx -y

if [ $? -eq 0 ]; then
  log_message "Instalação do NGINX concluida."
else
  log_message "ERRO: Falha na instalação do NGINX."
fi


# Configuração do proxy reverso no Nginx
sudo tee /etc/nginx/sites-available/reverse-proxy.conf > /dev/null <<EOT
server {
  listen 80;
  listen [::]:80;
  server_name ${subdominiodocliente}.vitrinededados.com;
  access_log /tmp/nginx.log_acesso;
  error_log /tmp/nginx.log_erro debug;
  client_max_body_size 10M;

  location ^~/ {
    proxy_pass http://127.0.0.1:3000;
  }
}
EOT

sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-available/reverse-proxy.conf /etc/nginx/sites-enabled/reverse-proxy.conf

if [ $? -eq 0 ]; then
  log_message "Configuração do NGINX concluida."
else
  log_message "ERRO: Falha na configuração do NGINX."
fi


# Instalação do PostgreSQL
log_message "Iniciando a instalação do PostgreSQL..."
sudo apt update
sudo apt install postgresql-12 postgresql-contrib -y

if [ $? -eq 0 ]; then
  log_message "Instalação do Postgres concluida."
else
  log_message "ERRO: Falha na Instalação do Postgres."
fi


# Alteração da porta do PostgreSQL
log_message "Iniciando a configuração do PostgreSQL..."
sudo sed -i 's/port = 5432/port = 12396/' /etc/postgresql/12/main/postgresql.conf
sudo service postgresql restart

if [ $? -eq 0 ]; then
  log_message "Configuração do Postgres concluida."
else
  log_message "ERRO: Falha na Configuração do Postgres."
fi

# Instalação do Citus
log_message "Iniciando a instalação do Citus..."
sudo apt-get install protobuf-c-compiler -y
sudo apt-get install libprotobuf-c0-dev -y
sudo apt-get install libprotobuf-c-dev -y

curl https://install.citusdata.com/community/deb.sh > add-citus-repo.sh
sudo bash add-citus-repo.sh
sudo apt-get install postgresql-12-citus-10.2 -y

if [ $? -eq 0 ]; then
  log_message "Instalação do Citus concluida."
else
  log_message "ERRO: Falha na Instalação do Citus."
fi

# Configuração do Citus
log_message "Iniciando a configuração do Citus..."

# Editando o arquivo postgresql.conf para incluir as extenções
sudo sed -i 's/#shared_preload_libraries = ''/shared_preload_libraries = 'citus, pg_stat_statements'/' /etc/postgresql/12/main/postgresql.conf
sudo service postgresql restart

if [ $? -eq 0 ]; then
  log_message "Configuração do Citus concluida."
else
  log_message "ERRO: Falha na Configuração do Citus."
fi

# Ativando o Citus no banco de dados
log_message "Iniciando a ativação do Citus no banco de dados..."
sudo -u postgres psql -c "CREATE EXTENSION citus; CREATE EXTENSION pg_stat_statements;"

if [ $? -eq 0 ]; then
  log_message "Ativação do Citus no banco de dados concluida."
else
  log_message "ERRO: Falha na Ativação do Citus no banco de dados."
fi



# Configuração do certificado digital no Nginx (substitua os valores pelos seus próprios)
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/metabase.key -out /etc/ssl/certs/metabase.crt -subj "/C=US/ST=State/L=City/O=Organization/OU=Department/CN=${subdominiodocliente}.vitrinededados.com"

sudo tee /etc/nginx/sites-available/reverse-proxy.conf > /dev/null <<EOT
server {
  listen 80;
  listen [::]:80;
  server_name ${subdominiodocliente}.vitrinededados.com;
  return 301 https://\$host\$request_uri;
}

server {
  listen 443 ssl http2;
  listen [::]:443 ssl http2;
  server_name ${subdominiodocliente}.vitrinededados.com;
  access_log /var/log/nginx/access.log;
  error_log /var/log/nginx/error.log;

  ssl_certificate /etc/ssl/certs/metabase.crt;
  ssl_certificate_key /etc/ssl/private/metabase.key;

  location / {
    proxy_pass http://localhost:3000;
    proxy_set_header Host \$host;
    proxy_set_header X-Real-IP \$remote_addr;
    proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto \$scheme;
  }
}
EOT

sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-available/reverse-proxy.conf /etc/nginx/sites-enabled/reverse-proxy.conf

sudo systemctl reload nginx

# Instalação do Docker
sudo apt-get update
sudo apt-get remove docker docker-engine docker.io containerd runc -y
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io -y

# Instalação do Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Clone do repositório do Airbyte
cd /opt
git clone https://github.com/airbytehq/airbyte.git
cd airbyte

# Configuração do arquivo .env do Airbyte (substitua os valores pelos seus próprios)
tee .env > /dev/null <<EOT
# Airbyte Configuration
AIRBYTE_VERSION=0.32.0
AIRBYTE_ROLE=standard

# Database Configuration
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_USER=airbyte
DATABASE_PASSWORD=password
DATABASE_DB=airbyte

# Docker Configuration
DOCKER_NETWORK=airbyte_default
EOT

# Construção e inicialização dos containers do Airbyte
docker-compose build
docker-compose up -d

# Fim do script
echo "Script concluído."
