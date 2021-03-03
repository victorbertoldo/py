# -*- coding: utf-8 -*-

import sqlalchemy as sqla
import pandas as pd

# Criando a engines de conexão com banco de dados
engine_origin = sqla.create_engine("mssql+pyodbc://system_prd:123456@./SOURCE?driver=SQL Server")
engine_destin = sqla.create_engine("postgresql+psycopg2://postgres:postgres@localhost/dw")

pedidos = pd.read_sql(sql="SELECT * FROM fato_pedidos", con=engine_origin)

produtos = pd.read_sql(sql="SELECT * FROM dim_produtos", con=engine_origin)

lojas = pd.read_sql(sql="SELECT * FROM dim_lojas", con=engine_origin)

obt = pd.merge(left=pedidos, right=produtos, how='inner', left_on='produto', right_on='id')
obt = pd.merge(left=obt, right=lojas, how='inner', left_on='loja', right_on='id')

# Limpando colunas desnecessarias
obt.drop(columns=['id_x','id_y', 'produto_x', 'id', 'loja'], inplace=True)

# Alterando a ordem das colunas
obt = obt[['produto_y', 'valor', 'data', 'cidade', 'estado', 'logradouro' ]]

# Renomeando colunas
obt.rename(columns={'produto_y': 'Produto', 'valor': 'Preço', 'data': 'Data', 'cidade': 'Cidade', 'estado': 'UF', 'logradouro': 'Endereço' }, inplace=True)

# Calculando o chunksize máximo
cs = 2097 // len(obt.columns) # pegando o inteiro da divisão

if cs > 1000:
    cs = 1000
else:
    cs = cs    
# Carregar os dados no destino


obt.to_sql(name='obt_pedidos', con=engine_destin, if_exists='replace', index=False, chunksize=cs)