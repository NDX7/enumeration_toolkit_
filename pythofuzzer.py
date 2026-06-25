import requests ,sys

res=requests.get("https://api.airlines.bugbountymasterclass.com/")
print(res)
data=res.json()
print(data)

