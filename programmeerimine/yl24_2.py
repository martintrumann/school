import urllib3, json, re
from bs4 import BeautifulSoup as BS

url = "https://ametikool.siseveeb.ee/veebivormid/tunniplaan/tunniplaan?oppegrupp=424"

page = urllib3.PoolManager().request('GET',url).data
soup = BS(page, "lxml")

scripts = soup.find_all('script')

script = scripts[24]
sscript = str(script)

print(re.sub('^(.*?)?(events.*)', "\\2", str(script)))

#pyscript = json.loads(script)
