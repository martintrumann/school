import urllib3, json, re
from bs4 import BeautifulSoup

def cleanhtml(text):
  return ''.join(xml.etree.ElementTree.fromstring(text).itertext())

#url = "https://ametikool.siseveeb.ee/veebivormid/tunniplaan/tunniplaan?oppegrupp=424"
url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
page = urllib3.PoolManager().request('GET',url).data
soup = BeautifulSoup(page, "lxml")

titles = soup.find_all('td', 'titleColumn')

for title in titles:
	ctitle = cleanhtml(title)
	print(ctitle)
