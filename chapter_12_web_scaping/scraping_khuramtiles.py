import requests, bs4

res = requests.get("https://software.khuramtiles.com/Reports/account_ledger")
res.raise_for_status()
kt_soup = bs4.BeautifulSoup(res.text, "html.parser")
kt_elemt = kt_soup.select("table")
print(type(kt_elemt))
print(str(kt_elemt))
print(len(kt_elemt))
