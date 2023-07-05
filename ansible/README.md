# Começando com o ansible

A primeira coisa é instalar o ansible.

```bash	
sudo apt-get install ansible
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible -y
```
Tlvz seja preciso fazer um downgrade no markupsafe
```bash
pip3 install --no-cache-dir "MarkupSafe==1.1.1"
```

Agora precisamos editar o arquivo `/etc/ansible/hosts` e adicionar o ip do servidor que queremos configurar.

```bash
sudo vim /etc/ansible/hosts
```

Adicione o ip do servidor que queremos configurar.

```bash
[grupo]
endereço_ip ansible_user=usuario ansible_ssh_private_key_file=/home/usuario/.ssh/id_rsa
```