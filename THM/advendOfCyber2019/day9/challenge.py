#! /bin/python3.12

import requests

url = "http://10.10.169.100:3000/"
value = ""
nextPage = ""
while nextPage!= "end":
	page = requests.get(f"{url}{nextPage}")
	content = page.text.split('"')
	nextPage = content[len(content)-2]
	print(f"content = {content}\n nextPage= {nextPage}" )
	value += content[3]
print(value)
