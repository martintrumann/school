import urllib3, demjson, re, datetime
from bs4 import BeautifulSoup as BS

url = "https://ametikool.siseveeb.ee/veebivormid/tunniplaan/tunniplaan?oppegrupp=424"
page = urllib3.PoolManager().request('GET',url).data
soup = BS(page, "lxml")
scripts = soup.find_all('script')
script = scripts[24]
sscript = str(script).replace("\n", "")
JSON = re.sub('^(.*?events: )?(.*)?(,\s*lessons.*)', "\\2", sscript)
djson = demjson.decode(JSON)

lessons = []
for lesson in djson:
    ldict = {}
    for key, value in lesson.items():
        if key == "title":
            values = value.split(";")
            lfname = []
            for x in values:
                xsoup = BS(x)
                try:
                    name = xsoup.span.string
                except:
                    name = xsoup.p.string
                lfname.append(name)
            ldict["Name"] = lfname[0]
            ldict["Teacher"] = lfname[-2]
            ldict["Classroom"] = lfname[-1]
        if key == "start":
            date_time = value.split("T")
            date = date_time[0]
            year = int(date.split("-")[0])
            month = int(date.split("-")[1])
            day = int(date.split("-")[2])

            time_offset = date_time[1].split("+")
            time = time_offset[0]
            h = int(time.split(":")[0])
            min = int(time.split(":")[1])
            sec = int(time.split(":")[2])

            offset = time_offset[1]
            offset_h_min = offset.split(":")
            offset_h = offset_h_min[0]
            offset_min = offset_h_min[1]
            offset_hmin = int(offset_h + offset_min)

            xtime = datetime.datetime(year, month, day, h, min, sec)

            ldict["Start"] = xtime.strftime("%A, %d.%B %H:%M")
    lessons.append(ldict)
print(lessons)
