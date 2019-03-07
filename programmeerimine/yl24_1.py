import urllib3, json, re
from bs4 import BeautifulSoup

#url = "https://ametikool.siseveeb.ee/veebivormid/tunniplaan/tunniplaan?oppegrupp=424"
url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
page = urllib3.PoolManager().request('GET',url).data
soup = BeautifulSoup(page, "lxml")

titles = soup.find_all('td', 'titleColumn')

i = 1
for title in titles:
	stitle = BeautifulSoup(str(title), "lxml")
	print(i, stitle.a.string, stitle.span.string)
	i = i + 1
