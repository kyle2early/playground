##plasticnews

import urllib2
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

url="http://www.plasticsnews.com/resin/commodity-thermoplastics/current-pricing"
page=urllib2.urlopen(url).read()

resins = ["HDPE","LDPE","LLDPE","PS","PVC","PP","ABS","Acrylic","PET"]
tablesIDs = ["data-table_" + x for x in resins]
tables=soup.find('table',{'id':[tablesIDs]})

resin=[]
grade=[]
low_low=[]
low_high=[]
high_low=[]
high_high=[]
dict={}

for i in range(9):
    rows = soup.find("table",{"id":tablesIDs[i]}).find("tbody").find_all("tr")

    for row in rows:
        cells=row.find_all("td")
        resin.append(resins[i])
        grade.append(cells[0].text)
        low_low.append(cells[2].text.replace(u"\u2014","-").split("-")[0])
        low_high.append(cells[2].text.replace(u"\u2014","-").split("-")[1])
        high_low.append(cells[4].get_text().replace(u"\u2014","-").split("-")[0])
        high_high.append(cells[4].get_text().replace(u"\u2014","-").split("-")[1])
        dict['resin'] = resin
        dict['grade'] = grade
        dict['low_low'] = low_low
        dict['low_high'] = low_high
        dict['high_low'] = high_low
        dict['high_high'] = high_high

df = pd.DataFrame.from_dict(dict)
df = df.infer_objects()
import time
timestr = time.strftime("%Y%m%d_%H%M%p")
df.to_csv("plasticnews.csv_"+timestr)

    # dat['grade','low_low','low_high','high_low','high_high'] = [grade, low_low, low_high, high_low, high_high]
#     grade.append(rn1)
#     low.append(rn2)
#     high.append(rn3)
# #
# low_low = []
# test = pd.DataFrame()
# for i in range(len(low)):
#     low_low.append(low[i].split("-")[0])
#     test['low'] = low[i].split("-")[0]

# Resin_Grade = table_PVC.find_all('td', {'class':'resin-subtype'})
#
# tds = table_PVC.find_all('td',{'class':'resin-vol'})
