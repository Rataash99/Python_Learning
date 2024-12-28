import requests as req

url = "https://portfolio.wealthmaker.in/wmapi_live/wealthmakerapikit.svc/generatetoken"

data = {
    "Source": "7",
    "UserId": "produser",
    "Password": "5pAm(gHw"
}
try:
    response = req.post(url, json = data)

    if response.status_code == 200:
        data = response.json()
        print("\n\nData : ", data, "\n\n")

    else :
        print(f"failed to fetch data : {response.status_code}")
        print(f"Error : {response.text}")

except Exception as err: 
    print(f"Some Error has occured : {err}")