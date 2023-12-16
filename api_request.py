import requests
import json


def api_request(moeda_origem):

    # Pegando a chave da api
    with open('config.json', 'r') as arquivo:
        configuracoes = json.load(arquivo)
    api_key = configuracoes.get('api_key')

    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{moeda_origem}'

    response = requests.get(url)
    data = response.json()

    return data
