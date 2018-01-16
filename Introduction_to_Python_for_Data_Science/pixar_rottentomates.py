#project ideas (stolen from r/dataisbeautiful) :: disney/pixar films & rotten tomatoes ratings; bubble size by opening box office revenue;
#
import urllib2
from bs4 import BeautifulSoup
import csv
import pandas as pd
import matplotlib.pyplot as plt
import sys      ## The following is a HORRIBLE HACK to unicode error at box_office sections
reload(sys)
sys.setdefaultencoding('utf8')

#Fetching list of films & release dates
url = "https://en.wikipedia.org/wiki/List_of_Pixar_films"  # change to whatever your url is

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "lxml")

release_dates = soup.find_all("table")[0]

with open('output.txt', 'w') as f:
    for tr in release_dates.find_all('tr')[2:]:
        tds = tr.find_all('td')
        f.write("%s, %s\n" % \
              (tds[1].text.replace(',',""), tds[2].text))

pixar_cols = ['Film', 'Release Month','Release Yr']

pixar_releases = pd.read_csv("output.txt", names=pixar_cols)

# scrape rotten tomaties reviews

rotten = soup.find_all("table")[2]

with open('output_reception.txt', 'w') as f:
    for tr in rotten.find_all('tr')[2:]:
        tds = tr.find_all('td')
        f.write("%s, %s\n" % \
              (tds[0].text.replace(',',""), tds[1].text.replace('%',"")))

pixar_reception = pd.read_csv("output_reception.txt", names=['Film','Rotten Tomatoes'])

box_office = soup.find_all("table")[3]

with open('output_boxoffice.txt', 'w') as f:
    for tr in box_office.find_all('tr')[2:]:
        tds = tr.find_all('td')
        f.write("%s, %s, %s\n" % \
              (tds[0].text.replace(',',""), tds[3].text.replace('$',"").replace('million',"").replace(',',"").strip(), tds[4].text.replace(',',"").replace('$',"").replace('million',"").replace('[30]',"").replace('[31]',"").strip()))

pixar_monies = pd.read_csv("output_boxoffice.txt", names=['Film','NA Gross','World Gross'])

pixar_all = pd.merge(pd.merge(pixar_monies, pixar_reception, on = 'Film'), pixar_releases, on = 'Film')          #join dataframe along subject value

# Plotting DataFrame
print(pixar_all)
pixar_all.to_csv('pixar_all.csv')
pixar_all.plot(kind = 'scatter', x = 'Release Yr', y = 'Rotten Tomatoes',title='Earnings for Pixar Films in North America',s=pixar_all['NA Gross']*2,grid=True,color=pixar_all['NA Gross'],cmap='GnBu')
plt.colorbar

# pixar_all.to_csv('pixar_all.csv')
# pixar_all.plot(kind = 'scatter', x = 'Release Yr', y = 'Rotten Tomatoes',title='Earnings for Pixar Films in North America',s=pixar_all['NA Gross']*2,grid=True,c=pixar_all['NA Gross'],alpha=0.8,cmap='GnBu')
# cb=plt.colorbar(shrink=0.9)
# cb.set_label('Boxoffice Gross Earnings')
# plt.colorbar

# Identify top3 gross films
pixar_top3 = pixar_all.sort_values(by=['NA Gross'], ascending=False).head(3)

# plt.annotate(pixar_top3.iloc[1]['Film'],xy=(pixar_top3.iloc[1]['Release Yr'],pixar_top3.iloc[1]['Rotten Tomatoes']),xytext=(-20,20),textcoords='offset points',arrowops=dict(arrowstyle='-->', connectionstyle='arc3,rad=0'))

# Annotate the plot with top3 gross films
for index, row in pixar_top3.iterrows():
    plt.annotate(row['Film'],xy=(row['Release Yr'],row['Rotten Tomatoes']),xytext=(-30,30),textcoords='offset points',arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0'),bbox=dict(facecolor='yellow',boxstyle='round,pad=0.2'))

# Identify bottom2 gross
pixar_bottom3 = pixar_all.sort_values(by=['NA Gross'], ascending=False).tail(2)
for index, row in pixar_bottom3.iterrows():
    plt.annotate(row['Film'],xy=(row['Release Yr'],row['Rotten Tomatoes']),xytext=(-25,-25),textcoords='offset points',arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0'),bbox=dict(facecolor='white',boxstyle='round,pad=0.2'))


# Save plot
plt.savefig("pixar_NA.png")
# show plot

plt.show()

# Histogram of the data
pixar_all['NA Gross'].plot.hist(alpha=0.5, grid=True, title='Pixar Box Office earnings in North America ')
plt.legend(['[USD]'])
plt.savefig("pixar_NA_histogram.png")
plt.show()

#insert average Rotten tomatoes line! pixar_all['Rotten Tomatoes'].mean()
