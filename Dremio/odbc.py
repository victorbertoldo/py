import pyodbc
import pandas

host = '10.0.1.205'
port = 31010
uid = 'dremio'
pwd = 'dR3m!0serV&r'
driver = 'Dremio Connector'

cnxn = pyodbc.connect("Driver={};ConnectionType=Direct; \
                    HOST={};PORT={};AuthenticationType=Plain;UID={};PWD={}".format(
                    driver, host, port, uid, pwd), autocommit=True)

sql = '''SELECT * FROM "ANTT".Emitente.Emitente_Full
        LIMIT 10'''

dataframe = pandas.read_sql(sql, cnxn)
print(dataframe.head())
