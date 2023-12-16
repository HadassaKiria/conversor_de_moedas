import api_request


def conversion(moeda_origem, moeda_destino, valor):
    data = api_request.api_request(moeda_origem)

    taxa_cambio = data['conversion_rates'][moeda_destino]

    return valor * taxa_cambio
