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
sudo sed -i 's/#Port 22/Port 1584/' /etc/ssh/sshd_config
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
# Executa o comando e obtém a saída
java_path=$(sudo update-alternatives --config java | grep -o '/.*/bin/java')

# Verifica se o comando retornou um caminho válido
if [ -n "$java_path" ]; then
  # Extrai o diretório pai do caminho do Java
  java_home=$(dirname "$(dirname "$java_path")")
  
  # Verifica se a linha já existe no arquivo /etc/environment
  if grep -q "^JAVA_HOME=" /etc/environment; then
    # Atualiza a linha existente
    sudo sed -i "s|^JAVA_HOME=.*$|JAVA_HOME=\"$java_home\"|" /etc/environment
  else
    # Adiciona uma nova linha no arquivo
    echo "JAVA_HOME=\"$java_home\"" | sudo tee -a /etc/environment >/dev/null
  fi
  
  # Exibe a variável JAVA_HOME atualizada
  echo "JAVA_HOME configurado para: $java_home"
else
  echo "ERRO: Não foi possível determinar o caminho do Java."
fi
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

config_file="/etc/rsyslog.d/metabase.conf"
program_name="metabase"

# Verifica se o arquivo de configuração já existe
if [ -f "$config_file" ]; then
  echo "O arquivo de configuração $config_file já existe. Removendo..."
  sudo rm "$config_file"
fi

# Cria o novo arquivo de configuração
sudo touch "$config_file"
sudo chmod 644 "$config_file"

# Adiciona as informações ao arquivo de configuração
echo "if \$programname == '$program_name' then $log_file" | sudo tee -a "$config_file" >/dev/null
echo "& stop" | sudo tee -a "$config_file" >/dev/null

echo "Configuração concluída. O arquivo $config_file foi criado com sucesso."

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
  access_log /var/log/nginx/access.log;
  error_log /var/log/nginx/error.log debug;

  client_max_body_size 10M;

  location ^~/ {
    proxy_pass http://127.0.0.1:3000;
  }
}
EOT

sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-available/reverse-proxy.conf /etc/nginx/sites-enabled/reverse-proxy.conf

sudo chown www-data.adm /var/log/nginx/*
sudo chmod 640 /var/log/nginx/*
sudo service nginx restart

if [ $? -eq 0 ]; then
  log_message "Configuração primária (80) do NGINX concluida."
else
  log_message "ERRO: Falha na configuração primária (80) do NGINX."
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
sudo sed -i 's/port = 5432/port = 12396/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo systemctl stop postgresql >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo systemctl start postgresql >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

sleep 1m

if lsof -i :12396 | grep LISTEN >/dev/null; then
    log_message "Port 12396 is listening"
else
    log_message "Port 12396 is not listening"
fi


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
sudo sed -i "s|#shared_preload_libraries = ''|shared_preload_libraries = 'citus, pg_stat_statements'|" /etc/postgresql/12/main/postgresql.conf

# Incluir as configurações do pg_stat_statements pg_stat_statements.max = 10000 e pg_stat_statements.track = all
sudo sed -i "/shared_preload_libraries/ a pg_stat_statements.max = 10000" /etc/postgresql/12/main/postgresql.conf
sudo sed -i "/pg_stat_statements.max = 10000/ a pg_stat_statements.track = all" /etc/postgresql/12/main/postgresql.conf

# O parametro abaixo determina quando a query será cortada do acompanhamento de atividade do pg_stat_statements
# sudo sed -i 's/#track_activity_query_size = 1024/track_activity_query_size = 1024/' /etc/postgresql/12/main/postgresql.conf # parametro opcional

sudo service postgresql restart

if [ $? -eq 0 ]; then
  log_message "Configuração do Citus concluida."
else
  log_message "ERRO: Falha na Configuração do Citus."
fi

# Ativando o Citus no banco de dados
log_message "Iniciando a ativação do Citus no banco de dados..."
# Specify the database name and port
database_name="dw"
database_port="12396"

# Create the database
sudo -u postgres psql -c "CREATE DATABASE $database_name;"

# alterar configuração para permitir login de usuarios
sudo sed -i 's/^\([^#]*\)trust/\1md5/g' /etc/postgresql/12/main/pg_hba.conf
sudo sed -i 's/^\([^#]*\)peer/\1md5/g' /etc/postgresql/12/main/pg_hba.conf

sudo service postgresql restart
# Connect to the newly created database and execute the command
sudo -u postgres psql -d $database_name -p $database_port -c "CREATE EXTENSION citus; CREATE EXTENSION pg_stat_statements;"

if [ $? -eq 0 ]; then
  log_message "Ativação do Citus no banco de dados concluida."
else
  log_message "ERRO: Falha na Ativação do Citus no banco de dados."
fi


log_message "Iniciando a instalação do Docker..."
log_message "Update package information..."
sudo apt-get update

# Remove existing Docker installations
log_message "Remove existing Docker installations..."
sudo apt-get remove docker docker-engine docker.io containerd runc -y >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

if [ $? -eq 0 ]; then
  log_message "Configurações do Docker removidas."
else
  log_message "ERRO: Falha na remoção das configurações pre-existentes do docker."
fi

# Install dependencies
log_message "Install dependencies..."
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release -y >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

if [ $? -eq 0 ]; then
  log_message "Dependências do Docker instaladas."
else
  log_message "ERRO: Falha na instalação das dependências do docker."
fi

# Add Docker GPG key
log_message "Add Docker GPG key..."
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

if [ $? -eq 0 ]; then
  log_message "Chave GPG do Docker adicionada."
else
  log_message "ERRO: Falha na adição da chave GPG do docker."
fi

# Add Docker repository
log_message "Add Docker repository..."
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

if [ $? -eq 0 ]; then
  log_message "Repositório do Docker adicionado."
else
  log_message "ERRO: Falha na adição do repositório do docker."
fi

# Update package information (again)
log_message "Update package information (again)..."
sudo apt-get update >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

if [ $? -eq 0 ]; then
  log_message "Informações do pacote atualizadas."
else
  log_message "ERRO: Falha na atualização das informações do pacote."
fi

# Install Docker
log_message "Install Docker..."
sudo apt-get install docker-ce docker-ce-cli containerd.io -y

if [ $? -eq 0 ]; then
  log_message "Docker instalado."
else
  log_message "ERRO: Falha na instalação do docker."
fi

# Install Docker Compose
log_message "Install Docker Compose..."
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo chmod +x /usr/local/bin/docker-compose >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

if [ $? -eq 0 ]; then
  log_message "Docker Compose instalado."
else
  log_message "ERRO: Falha na instalação do docker compose."
fi

# Print Docker and Docker Compose versions
if [ $? -eq 0 ]; then
  log_message "Versão do Docker:"
  docker --version
else
  log_message "ERRO: Falha na obtenção da versão do docker."
fi

docker --version >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

if [ $? -eq 0 ]; then
  log_message "Versão do Docker Compose:"
  docker-compose --version
else
  log_message "ERRO: Falha na obtenção da versão do docker compose."
fi

docker-compose --version >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

if [ $? -eq 0 ]; then
  log_message "Instalação do Docker concluida."
else
  log_message "ERRO: Falha na instalação do docker."
fi

# Começar a configuração do airbyte
# Para isso temos que instalar o git
log_message "Iniciando a instalação do Git..."
sudo apt-get install git -y >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

if [ $? -eq 0 ]; then
  log_message "Instalação do Git concluida."
else
  log_message "ERRO: Falha na instalação do Git."
fi

# clone Airbyte from GitHub
log_message "Iniciando o clone do Airbyte do GitHub..."
cd /opt
sudo git clone https://github.com/airbytehq/airbyte.git >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
cd airbyte
# escrever uma msg no log
log_message "Pasta atual do log"
# printar a pasta atual no log para ver se está no lugar certo
pwd >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

if [ $? -eq 0 ]; then
  log_message "Clone do Airbyte do GitHub concluido."
else
  log_message "ERRO: Falha no clone do Airbyte do GitHub."
fi

# Configurações para funcionamento do airbyte
log_message "Iniciando a configuração do Airbyte..."
sudo addgroup airbyte >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo adduser --system --ingroup airbyte --disabled-login airbyte >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo chown -R airbyte:airbyte /opt/airbyte/ >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

if [ $? -eq 0 ]; then
  log_message "Configuração de permissionamento Airbyte concluida."
else
  log_message "ERRO: Falha na configuração de permissionamento do Airbyte."
fi

# primeira execução do airbyte para baixar as dependencias
log_message "Iniciando a primeira execução do Airbyte..."

# primeiro precisamos adicionar permissão de execução para o ./run-ab-platform.sh
sudo chmod +x /opt/airbyte/run-ab-platform.sh >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
# alterar o jeito de subir os dockers sem travar o terminal
sudo sed -i 's/docker compose up/docker compose up -d/g' run-ab-platform.sh
# executar o script em silencio sem travar o terminal
sudo ./run-ab-platform.sh >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

if [ $? -eq 0 ]; then
  log_message "Primeira execução do Airbyte concluida."
else
  log_message "ERRO: Falha na primeira execução do Airbyte."
fi

# sleep de 3 minutos para dar tempo de baixar as dependencias
log_message "Iniciando o sleep de 3 minutos..."
sleep 10m

# Parar ambiente airbyte via docker-compose
log_message "Iniciando a parada do ambiente Airbyte..."
sudo docker compose down >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

# voltar o .sh ao normal
sudo sed -i 's/docker compose up -d/docker compose up/g' run-ab-platform.sh

if [ $? -eq 0 ]; then
  log_message "Parada do ambiente Airbyte concluida."
else
  log_message "ERRO: Falha na parada do ambiente Airbyte."
fi

# Alterar a senha do airbyte
log_message "Iniciando a alteração da senha e do usuario do Airbyte..."
sudo sed -i 's/BASIC_AUTH_USERNAME=.*/BASIC_AUTH_USERNAME=vitre/' .env >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/BASIC_AUTH_PASSWORD=.*/BASIC_AUTH_PASSWORD=v!tr3#B0ldZ/' .env >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

if [ $? -eq 0 ]; then
  log_message "Alteração da senha e do usuario do Airbyte concluida."
else
  log_message "ERRO: Falha na alteração da senha e do usuario do Airbyte."
fi

log_message "Iniciando a configuração do Airbyte como serviço..."
sudo touch /var/log/airbyte.log >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo chown syslog:adm /var/log/airbyte.log >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

sudo touch /etc/default/airbyte >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo chmod 640 /etc/default/airbyte >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

sudo touch /etc/systemd/system/airbyte.service >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo touch /etc/rsyslog.d/airbyte.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

sudo chmod 666 /var/run/docker.sock

# Edit airbyte systemd service file
log_message "Iniciando a edição do arquivo de serviço do Airbyte..."
sudo ex -s /etc/systemd/system/airbyte.service <<EOF
a
[Unit]
Description=airbyte
Requires=docker.service
After=docker.service
After=network.target

[Service]
User=airbyte
WorkingDirectory=/opt/airbyte/
#ExecStartPre=/usr/local/bin/docker-compose down
#ExecStartPre=/usr/local/bin/docker-compose rm -f
ExecStart=/opt/airbyte/run-ab-platform.sh
#ExecStop=

#Type=simple
#StandardOutput=syslog
#StandardError=syslog
#SyslogIdentifier=airbyte
#SuccessExitStatus=143
#TimeoutStopSec=1200
#Restart=on-failure



[Install]
WantedBy=multi-user.target

.
wq
EOF 

if [ $? -eq 0 ]; then
  log_message "Edição do arquivo de serviço do Airbyte concluida."
else
  log_message "ERRO: Falha na edição do arquivo de serviço do Airbyte."
fi


# Edit airbyte rsyslog configuration file
log_message "Iniciando a edição do arquivo de configuração do Airbyte..."
sudo ex -s /etc/rsyslog.d/airbyte.conf <<EOF
a
if \$programname == 'airbyte' then /var/log/airbyte.log
& stop

.
wq
EOF

if [ $? -eq 0 ]; then
  log_message "Edição do arquivo de configuração do Airbyte concluida."
else
  log_message "ERRO: Falha na edição do arquivo de configuração do Airbyte."
fi

# Restart syslog
log_message "Iniciando a reinicialização do syslog..."
sudo systemctl restart rsyslog.service >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

if [ $? -eq 0 ]; then
  log_message "Reinicialização do syslog concluida."
else
  log_message "ERRO: Falha na reinicialização do syslog."
fi

# Reload systemd daemon
log_message "Iniciando a reinicialização do daemon do systemd..."
sudo systemctl daemon-reload >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

# Enable and start airbyte service
log_message "Iniciando a habilitação e inicialização do serviço do Airbyte..."
sudo systemctl enable airbyte.service >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo systemctl start airbyte.service >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

# Check the status of airbyte service
log_message "Iniciando a verificação do status do serviço do Airbyte..."
sudo systemctl status airbyte.service >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

if [ $? -eq 0 ]; then
  log_message "Verificação do status do serviço do Airbyte concluida."
else
  log_message "ERRO: Falha na verificação do status do serviço do Airbyte."
fi

if [ $? -eq 0 ]; then
  log_message "Configuração do Airbyte como serviço concluida."
else
  log_message "ERRO: Falha na Configuração do Airbyte como serviço."
fi

# Começar a configuração do metabase para ssl https e certificado
log_message "Iniciando a configuração do Metabase para SSL e certificado..."
# Install Certbot and Nginx plugin
sudo apt-get update -y
sudo apt-get install software-properties-common -y
sudo add-apt-repository universe -y
sudo add-apt-repository ppa:certbot/certbot -y
sudo apt-get update -y
sudo apt-get install certbot python3-certbot-nginx -y

# Obtain SSL certificate
sudo certbot run --nginx --agree-tos -n -d ${subdominiodocliente}.vitrinededados.com --non-interactive --email victor@vitrinededados.com >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

# Test Nginx configuration
log_message "Iniciando a verificação da configuração do Nginx..."
sudo nginx -t >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

# Reload Nginx
log_message "Iniciando o reload do Nginx..."
sudo systemctl reload nginx >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)


if [ $? -eq 0 ]; then
  log_message "Configuração do Metabase para SSL e certificado concluida."
else
  log_message "ERRO: Falha na Configuração do Metabase para SSL e certificado."
fi

# Agora configurar o airbyte para funcionar com o https e certificado digital
log_message "Iniciando a configuração do Airbyte para SSL e certificado..."
# Generate SSL certificate using Certbot and configure Nginx
# Configuração do proxy reverso no Nginx
sudo tee /etc/nginx/sites-available/airbyte.conf > /dev/null <<EOT
server {
  listen 80;
  listen [::]:80;
  server_name airbyte-${subdominiodocliente}.vitrinededados.com;
  access_log /var/log/nginx/access.log;
  error_log /var/log/nginx/error.log debug;

  client_max_body_size 10M;

  location ^~/ {
    proxy_pass http://127.0.0.1:8000;
  }
}
EOT

sudo ln -s /etc/nginx/sites-available/airbyte.conf /etc/nginx/sites-enabled/airbyte.conf

sudo certbot run --nginx --agree-tos -n -d "airbyte-${subdominiodocliente}.vitrinededados.com" --non-interactive --email victor@vitrinededados.com >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

# Restart Nginx to apply the changes
log_message "Iniciando o restart do Nginx..."
sudo systemctl restart nginx


if [ $? -eq 0 ]; then
  log_message "Configuração do Airbyte para SSL e certificado concluida."
else
  log_message "ERRO: Falha na Configuração do Airbyte para SSL e certificado."
fi

# Instalação do pgadmin
log_message "Instalação do PGAdmin..."
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

sudo apt install pgadmin4 -y >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

log_message "Configurando o apache2 do PGAdmin..."

sudo sed -i 's/Listen 80/Listen 82/g' /etc/apache2/ports.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/Listen 443/Listen 449/g' /etc/apache2/ports.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

sudo service apache2 restart

# incluindo o pgadmin na configuração do nginx
sed -i.bkp 's/location/location\ pgadmin4\/\ {\n\tproxy_pass http:\/\/127.0.0.1:82\/pgadmin4\/;\n}\n  location/' /etc/nginx/sites-available/reverse-proxy.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

# após essa parte, é necessário fazer uma configuração manual do nginx para apontar para a porta que definimos para o apache2
# isso feito, rodar manualmente tbm o script: sudo /usr/pgadmin4/bin/setup-web.sh para configurar o pgadmin4

# Fim do script
echo "Script concluído."

log_message "Ir para pasta home."
cd $HOME
pwd >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
# agora precisamos dar permissão de execução para o arquivo de script configuração do dw `dw_configuration.sh`
sudo chmod +x dw_configuration.sh >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
# agora precisamos chamar a execução do script de configuração do dw `dw_configuration.sh`
sudo ./dw_configuration.sh >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)


# Fim do script