import requests
import plooconstants
server = f"{plooconstants.SERVER}/Deals"
token = plooconstants.API_KEY

headers = {
    "Authorization": f"Bearer {token}",
    "User-Key": token
}

deals_per_page = 300
page_number = 1
all_deals = []

while True:
    params = {
        "$top": deals_per_page,
        "$skip": (page_number - 1) * deals_per_page
    }

    response = requests.get(server, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if not data["value"]:
            # No more deals to fetch, break the loop
            break
        all_deals.extend(data["value"])
        page_number += 1
    else:
        # Handle the error here
        print(f"Request failed with status code {response.status_code}")
        break

# Now you have all the deals in `all_deals`
for item in all_deals:
    title = item["Title"] 
    print(title) #to print the title, for example

print(f"Total number of deals: {len(all_deals)}") #to print the amount of deals
