import pandas as pd
import json

csv = pd.read_csv('dados.csv')
print(csv.head())

json_var = dict(csv)

for i, j in json_var.items():
    print(i ,': ',j)
    

csv.to_json(orient='records', path_or_buf='json_.json')


app_json = json.dumps(json_var)
print(app_json)