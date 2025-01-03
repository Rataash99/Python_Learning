import requests as req

def fetch_data(url):
    res = req.get(url)

    data = []

    if res.status_code == 200:
        data = res.json()
    else:
        print(f"unable to fetch data, status of request : {res.status_code}")

    return data
