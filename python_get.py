import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

if response.status_code == 200 : 
    print("Response Data", response.json())

else :
    print(f"Failed to fetch data. status code : {response.status_code}")
