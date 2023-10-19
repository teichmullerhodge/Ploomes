import requests
import json
import plooconstants


total_amount = 0
number_of_quotes = 0

server = "https://api2.ploomes.com/Quotes"


token = plooconstants.API_KEY

headers = {
    
    "Authorization": f"Bearer {token}",
    "User-Key": token
    
    }

response = requests.get(server, headers=headers)


if response.status_code == 200:
    
        data = response.json()
        my_data = json.dumps(data, indent=4)
        #print(my_data) 
        for quotes in data['value']:
            number_of_quotes += 1
            total_amount += quotes['Amount']


else:
        # Handle the error here
        print(f"Request failed with status code {response.status_code}")

print(f"Number of quotes: {number_of_quotes}\nAmount: {total_amount}")
