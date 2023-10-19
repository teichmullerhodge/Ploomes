import requests
import json
import plooconstants

SERVER = f"{plooconstants.SERVER}/"
API_KEY = plooconstants.API_KEY
ENDPOINTS = []

def get_endpoints():

    URL = f"{SERVER}/Fields@Entities"
    token = API_KEY
    headers = {

        "Authorization" : "Bearer {token}",
        "User-Key" : token
    }

    response = requests.get(URL, headers=headers)

    if response.status_code == 200:

        data = response.json()
        for entities in data['value']:
            if entities['ApiUrl'] is not None:
               
                endpoints = entities['ApiUrl']     
                print(endpoints)
                ENDPOINTS.append(endpoints)

            else:
                continue

    else:
        
        print(f"Request failed with status code: {response.status_code}")


def get_account_data(endpoint):

    URL = f"{SERVER}/{endpoint}"
    token = API_KEY
    headers = {

        "Authorization" : "Bearer {token}",
        "User-Key" : token
    
    }

    response = requests.get(URL, headers=headers)

    if response.status_code == 200:
        data = response.json()
        json_str = json.dumps(data, indent=4)
        print(json_str)

    else:
        print(f"Request failed with status code: {response.status_code}")



get_endpoints()
for urls in ENDPOINTS:
    print("=" * 40)
    print(f"INFO ABOUT THE: {urls}")
    get_account_data(urls)

    #várias entidades não são necessárias para duplicação de contas, isso será ajustado.
    
