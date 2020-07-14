import json
import requests
import autenticacao as aut


print(dir())
aut.login(aut.username, aut.password)


def apiGet(endpoint):
    return json.loads(requests.get('{server}/api/v3/{endpoint}'
                                   .format(server=aut.dremioServer,
                                           endpoint=endpoint),
                                   headers=aut.headers).text)


def apiPost(endpoint, body=None):
    text = requests.post('{server}/api/v3/{endpoint}'
                         .format(server=aut.dremioServer,
                                 endpoint=endpoint),
                         headers=aut.headers, data=json.dumps(body)).text

    # a post may return no data
    if (text):
        return json.loads(text)
    else:
        return None


dados = apiGet('catalog/by-path/ANTT.Contratante."Contratante_Full"')
dados = dict(dados)

print(dados)
