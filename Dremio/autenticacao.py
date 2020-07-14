import json
import requests

username = 'dremio'
password = 'dR3m!0serV&r'
headers = {'content-type': 'application/json'}
dremioServer = 'http://10.0.1.205:9047'


def login(username, password):
    # we login using the old api for now
    loginData = {'userName': username, 'password': password}
    response = requests.post(f'{dremioServer}/apiv2/login',
                             headers=headers, data=json.dumps(loginData))
    data = json.loads(response.text)

    # retrieve the login token
    token = data['token']
    return {'content-type': 'application/json',
            'authorization': '_dremio{authToken}'.format(authToken=token)}


headers = login(username, password)
print(headers)
