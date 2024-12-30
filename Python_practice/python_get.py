import requests as req

url = "https://pokeapi.co/api/v2/pokemon/"

response = req.get(url)

if response.status_code == 200:
    print(response.json())

else:
    print(f"unable to fetch data, status of request : {response.status_code}")
