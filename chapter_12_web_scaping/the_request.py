import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
fake = requests.get("https://automatetheboringstufffake.com/files/rj.txt")
print(fake.raise_for_status())
print(type(res))
print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:250])
