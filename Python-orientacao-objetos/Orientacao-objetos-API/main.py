from fastapi import FastAPI, Query
import requests

appAPI = FastAPI()

@appAPI.get('/api/hello')
def hello_world():
    """
    Endpoint que exibe uma mensagem incrével do mundo na programção!
    """
    return {'Hello': 'World'}

@appAPI.get('/api/restaurantes')
def get_restaurantes(restaurante: str=Query(None)):
    """
    Endpoint para ver os cardápios dos resutanres
    """
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url=url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados':dados_json}

        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurante':restaurante, 'Cardapio':dados_restaurante}    
    else:
        return {f'Erro: {response.status_code} - {response.text}'}