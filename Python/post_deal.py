import requests

server = "https://api2.ploomes.com/Deals"
token = "YOUR API KEY"
headers = {

  "Authorization": f"Bearer {token}",
  "User-Key": token,
  "Content-Type": "application/json"
}



data = {

  "Title": "API-Python", #Deal title.
  "ContactId": 1234567, #if you want your deal to correspond to a specific contact, put the contact id here.
  "OwnerId" : 1234567, #id of the deal owner.
  "Amount" : 100, #deal amount in BRL.
  "PipelineId": 1234567 #PipeId.
  "StageId": 1234567 #StageId.

}

response = requests.post(server, headers=headers, json=data)

if response.status_code == 201:
  data = response.json()
  # Handle the response data here
  print(data)
else:
  # Handle the error here
  print(f"Request failed with status code {response.status_code}")
