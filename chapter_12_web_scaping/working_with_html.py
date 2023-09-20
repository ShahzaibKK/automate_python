import requests, bs4

# from Internet
res = requests.get("https://nostarch.com")
res.raise_for_status()
no_starch_soup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(no_starch_soup))
# from file in hard drive
example_file = open("example.html")
example_soup = bs4.BeautifulSoup(example_file.read(), "html.parser")
elmts = example_soup.select("p")
print(type(elmts))
print(len(elmts))
print(type(elmts[0]))
print(str(elmts[0]))
print(elmts[0].get_text())
print(elmts[0].attrs)
print(str(elmts[1]))
print(elmts[1].get_text())
print(elmts[1].attrs)
print(str(elmts[2]))
print(elmts[2].get_text())
print(elmts[2].attrs)
print()


# Getting Data From an Element's Attributes
elmts = example_soup.select("span")[1]
print(str(elmts))
print(elmts.get("id"))
print(elmts.get_text())
print(elmts.get("iddd_not_existent") == None)
