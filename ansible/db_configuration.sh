#!/bin/bash

# Nome do arquivo de log
log_file="db_script.log"

# Função para registrar mensagens de log
log_message() {
  echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" >> "$log_file"
}


log_message "Configurando o timezone..."
sudo timedatectl set-timezone America/Sao_Paulo

if [ $? -eq 0 ]; then
  log_message "Configuração do timezone concluída com sucesso."
else
  log_message "ERRO: Falha na configuração do timezone."
fi


sudo sed -i 's/shared_buffers = 128MB/shared_buffers = 2GB/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/#effective_cache_size = 4GB/effective_cache_size = 6GB/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/#work_mem = 4MB/work_mem = 41MB/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/#maintenance_work_mem = 64MB/maintenance_work_mem = 410MB/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/max_wal_size = 1GB/max_wal_size = 3GB/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/min_wal_size = 80MB/min_wal_size = 2GB/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/#checkpoint_completion_target = 0.5/checkpoint_completion_target = 0.9/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/#wal_buffers = -1/wal_buffers = -1/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/#random_page_cost = 4.0/random_page_cost = 4.0/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/#effective_io_concurrency = 1/effective_io_concurrency = 2/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/#max_worker_processes = 8/max_worker_processes = 8/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/#max_parallel_workers_per_gather = 2/max_parallel_workers_per_gather = 2/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/#max_parallel_workers = 8/max_parallel_workers = 2/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/#log_checkpoints = off/log_checkpoints = on/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/#log_connections = off/log_connections = on/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/#log_disconnections = off/log_disconnections = on/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/#logging_collector = off/logging_collector = on/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/#log_lock_waits = off/log_lock_waits = on/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/#log_min_duration_statement = -1/log_min_duration_statement = 10s/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)
sudo sed -i 's/#log_autovacuum_min_duration = -1/log_autovacuum_min_duration = 0/' /etc/postgresql/12/main/postgresql.conf >> >(tee -a "$log_file") 2> >(tee -a "$log_file" >&2)


# Editando o arquivo postgresql.conf para incluir as extenções
sudo sed -i "s|#shared_preload_libraries = ''|shared_preload_libraries = 'citus, pg_stat_statements'|" /etc/postgresql/12/main/postgresql.conf

# Incluir as configurações do pg_stat_statements pg_stat_statements.max = 10000 e pg_stat_statements.track = all
sudo sed -i "/shared_preload_libraries/ a pg_stat_statements.max = 10000" /etc/postgresql/12/main/postgresql.conf
sudo sed -i "/pg_stat_statements.max = 10000/ a pg_stat_statements.track = all" /etc/postgresql/12/main/postgresql.conf

sudo service postgresql restart
