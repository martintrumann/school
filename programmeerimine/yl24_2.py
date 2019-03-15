import urllib3, json, re
from bs4 import BeautifulSoup

url = "https://ametikool.siseveeb.ee/veebivormid/tunniplaan/tunniplaan?oppegrupp=424"

page = urllib3.PoolManager().request('GET',url).data
soup = BeautifulSoup(page, "lxml")

script = soup.find_all('script')[24].string

pyscript = json.loads(script)
