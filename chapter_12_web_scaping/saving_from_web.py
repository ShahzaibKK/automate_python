import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
try:
    res.raise_for_status()
except Exception as exe:
    print(f"There must be some broblem:\n{exe}")

with open("save_file.txt", "wb") as file:
    for chunk in res.iter_content(100000):
        file.write(chunk)
