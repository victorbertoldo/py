from elasticsearch import helpers, Elasticsearch
import csv


# Conexão ao Elastic
host = '10.0.10.7:9200'
es = Elasticsearch(
    host,
    http_auth=('elastic', 'EBkWmpXjVdwdaLtIv5wb'),
    scheme="https",
    port=443,
    verify_certs=False
    )

# ler o arquivo csv e com helpers.bulk inserir
with open('dados.csv', 'r') as dados:
    leitor = csv.DictReader(dados)
    res = helpers.bulk(es, leitor, index='chamados')
    # imprimir resultado do comando helpers.bulk
    print(len(res))
    print(res[0:-1])