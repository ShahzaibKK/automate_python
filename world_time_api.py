import requests, datetime


curl = "http://worldtimeapi.org/api/timezone/Asia/Karachi"

res = requests.get(curl)
json = res.json()
world_api_date_time = datetime.datetime.fromisoformat(json["datetime"])
print(world_api_date_time)
print(datetime.datetime.now().astimezone())
