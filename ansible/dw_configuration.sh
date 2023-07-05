#!/bin/bash

# Nome do arquivo de log
log_file="dw.log"

# Função para registrar mensagens de log
log_message() {
  echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" >> "$log_file"
}


# PostgreSQL connection parameters
DB_HOST="localhost"
DB_PORT="12396"  # Replace with your PostgreSQL port
DB_USER="postgres"
DB_NAME="dw"  # Replace with the desired database name


# Function to execute SQL commands
execute_sql() {
  psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -c "$1"
}

# Create database
log_message "Criando o banco de dados..."
execute_sql "CREATE DATABASE $DB_NAME;" >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

# Select the newly created database
log_message "Selecionando o banco de dados..."
execute_sql "SELECT pg_catalog.pg_database_size('$DB_NAME');" >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

execute_sql() {
  psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d "$DB_NAME" -c "$1"
}

# Create schemas
log_message "Iniciando a criação de schemas..."
execute_sql "CREATE SCHEMA landing;" >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
execute_sql "CREATE SCHEMA stage;" >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
execute_sql "CREATE SCHEMA intermediate;" >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
execute_sql "CREATE SCHEMA mart;" >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

if [ $? -eq 0 ]; then
  log_message "Criação de schemas concluída com sucesso."
else
  log_message "ERRO: Falha na criação de schemas."
fi

# Create users and assign privileges
log_message "Iniciando a criação de usuários e atribuição de privilégios..."
execute_sql "CREATE USER airbyte WITH PASSWORD 'a!rbyt3#fct94';"
execute_sql "GRANT CONNECT ON DATABASE dw TO airbyte;"
execute_sql "GRANT ALL PRIVILEGES ON SCHEMA landing TO airbyte;"
execute_sql "GRANT USAGE, CREATE ON SCHEMA landing TO airbyte;"

execute_sql "CREATE USER dbt_transform WITH PASSWORD 'dbt!3tR@nsf0rm';"
execute_sql "GRANT ALL PRIVILEGES ON SCHEMA stage, intermediate, mart TO dbt_transform;"
execute_sql "GRANT USAGE, CREATE ON SCHEMA stage, intermediate, mart TO dbt_transform;"

execute_sql "CREATE USER metabase_ui WITH PASSWORD 'm3taBase#9734';"
execute_sql "GRANT USAGE ON SCHEMA mart TO metabase_ui;"

# Grant privileges within the mart schema
execute_sql "GRANT SELECT, USAGE ON ALL TABLES IN SCHEMA mart TO metabase_ui;"
execute_sql "GRANT SELECT, USAGE ON ALL SEQUENCES IN SCHEMA mart TO metabase_ui;"

if [ $? -eq 0 ]; then
  log_message "Criação de usuários e atribuição de privilégios concluída com sucesso."
else
  log_message "ERRO: Falha na criação de usuários e atribuição de privilégios."
fi

echo "Schema and user creation completed successfully."


log_message "Iniciando a configuração do PostgreSQL..."
# Change the PostgreSQL password
NEW_DB_PASSWORD="dB#p0stGr3s!94"

execute_sql "ALTER USER postgres WITH PASSWORD '$NEW_DB_PASSWORD';" >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

# Change the operating system user password
NEW_OS_PASSWORD="dB#p0stGr3s!94"

echo "your_os_username:$NEW_OS_PASSWORD" | sudo chpasswd >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)

echo "Schema and user creation completed successfully."

if [ $? -eq 0 ]; then
  log_message "Configuração do PostgreSQL concluída com sucesso."
else
  log_message "ERRO: Falha na configuração do PostgreSQL."
fi