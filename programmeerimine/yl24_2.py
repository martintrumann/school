import urllib3, demjson, re
from bs4 import BeautifulSoup as BS

url = "https://ametikool.siseveeb.ee/veebivormid/tunniplaan/tunniplaan?oppegrupp=424"

page = urllib3.PoolManager().request('GET',url).data
soup = BS(page, "lxml")

scripts = soup.find_all('script')

script = scripts[24]

sscript = str(script).replace("\n", "")

JSON = re.sub('^(.*?events: )?(.*)?(,\s*lessons.*)', "\\2", sscript)

print(JSON)
#print(demjson.decode(JSON, return_errors="True"))
