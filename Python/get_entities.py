import requests
import json
import plooconstants

server = "https://api2.ploomes.com/Fields@Entities"
token = plooconstants.API_KEY
headers = {

    "Authorization": f"Bearer {token}",
    "User-Key": token
}

response = requests.get(server, headers=headers)

number_entities = 0

if response.status_code == 200:
    
    data = response.json()
    for entities in data['value']:
        json_str = json.dumps(entities, indent=4)
        

        print(json_str)
        number_entities += 1
else:
        # Handle the error here
        print(f"Request failed with status code {response.status_code}")

print(f"total de entidades: {number_entities}") #The total number of entities
