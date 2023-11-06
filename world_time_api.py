import requests, datetime


curl = "http://worldtimeapi.org/api/timezone/Asia/Karachi"

res = requests.get(curl)
json = res.json()
print(datetime.datetime.fromisoformat(json["datetime"]))
print(datetime.datetime.now())
