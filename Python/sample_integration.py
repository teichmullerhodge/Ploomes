import requests
import json
import plooconstants

PLOOMES_SERVER = "https://api2.ploomes.com/"
PLOOMES_TOKEN = plooconstants.API_KEY

APP_SERVER = "https://app.com/api/resources" #Exemplo aleatório
APP_TOKEN_AUTH = "<PRIVATE KEY>"


def get_data_by_endpoint(endpoint, top, skip, select, expand, filter, orderby):

    URL = f"{PLOOMES_SERVER}{endpoint}"
    API_KEY = PLOOMES_TOKEN

    headers = {

        "Authorization" : f"Bearer {API_KEY}",
        "User-Key" : API_KEY,
        "Content-Type" : "application/json"

    }

    parameters = {

        "$top" : top,
        "$skip" : skip,
        "$select" : select,
        "$expand" : expand,
        "$filter" : filter,
        "$orderby" : orderby
    }

    response = requests.get(URL, params=parameters, headers=headers)

    if response.status_code == 200:

        data = response.json()

        #....Manipular os dados JSON da forma que desejar antes de enviar para próxima plataforma
        #....Inserir condicionais, exemplo: Enviar dados apenas se valor não estiver vazio
        
        post_data_to_app(data)

        #ou atualizar dados

        patch_data_to_app(data, 12345) #exemplo de url de um item qualquer

    else:
        print(f"Request failed with status code: {response.status_code}")



def post_data_to_app(data_parameters):

    
    # Defina os dados a serem enviados no corpo da solicitação (se aplicável)
    data = {

        'param': data_parameters,
        #pode ser um array passado como argumento na função também.
    }

    # Defina os cabeçalhos da solicitação (se necessário)
    headers = {

        'Authorization': f'Bearer {APP_TOKEN_AUTH}',
        'Content-Type': 'application/json'
    }

# Faça a solicitação POST
    response = requests.post(APP_SERVER, json=data, headers=headers)

# Verifique o código de status da resposta
    if response.status_code == 200:
    # A solicitação foi bem-sucedida
        responseData = response.json()  # Supondo que a resposta está em formato JSON
        print(responseData) #printe no terminal demonstrando que a solicitação correu bem e quais dados foram enviados.
    else:
        print(f"A solicitação falhou com o código de status {response.status_code}")

def patch_data_to_app(new_values, item_url):

    url = f"{APP_SERVER/{item_url}}"  # Substitua pela URL real que você deseja usar

    # Defina os dados a serem enviados no corpo da solicitação (as atualizações que deseja fazer)
    
    data = {
    
        "key_to_update": new_values
    }

# Defina os cabeçalhos da solicitação (se necessário)
    headers = {

    "Authorization": f"Bearer {APP_TOKEN_AUTH}",
    "Content-Type": "application/json-patch+json"
    }

# Faça a solicitação PATCH
    response = requests.patch(url, json=data, headers=headers)

# Verifique o código de status da resposta
    if response.status_code == 200:
    # A solicitação foi bem-sucedida
        responseData = response.json()  # Supondo que a resposta está em formato JSON
        print(responseData) #printe no terminal demonstra que a atualização foi bem sucedida
    else:
        print(f"A solicitação PATCH falhou com o código de status {response.status_code}")