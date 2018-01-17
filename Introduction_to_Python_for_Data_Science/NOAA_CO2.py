# CO2 monthly mean records collectd by NOAA
# https://www.esrl.noaa.gov/gmd/ccgg/trends/data.html
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cols = ['year','mon','deci_date','average','inter','trend','no_days']
data = pd.read_csv("co2_mm_mlo.txt", sep="\s+ ", skiprows=range(0,72), names=cols)
data.head()
data.dtypes

dates = data.apply(lambda row: str(row.year)+str(row.mon)+str("1"), axis=1) # hack the date :(

data['datestamp'] = pd.to_datetime(dates)   # plug datestamp into dataframey

data.plot(x='datestamp',y='average'); plt.show()
#drop other columns
data=data.drop('no_days',1)
data=data.drop('trend',1)
data=data.drop('deci_date',1)

## data says unknown are marked -99.99
print(data[data.average==-99.99])

#change index to datestamp
data.index=data.datestamp

#plot relevant data
data.average[data.average !=-99.99].plot(grid=True)
plt.ylabel("CO2 Concentration, [ppm]")
plt.show()

#solve for the missing data- interpolation
#set -99.99 to inter value
data.average[data.average==-99.99]=data.inter

#group by years & decades
data_year=data.groupby(data.index.year).mean()
# data_decade=data.grouby(data.index.year//10)*10).mean() ##WRONG!S

#whats the average CO2 concentration per decade?
data.average.head(10).mean()


## linear regression
x=data_year.year
y=data_year.average
p1 = np.polyfit(x,y,1)  #linear regression
p2 = np.polyfit(x,y,2)  #polynomial regression
plt.plot(x,np.polyval(p1,x),"r--")
plt.plot(x,np.polyval(p2,x),"g--")
data_year.average.plot(grid=True)
plt.ylabel("CO2 Concentration, [ppm]")
plt.xlabel("")
plt.title("CO2 Levels over the years")
plt.legend(['linear regression','poly regression','monthly average'],loc='lower right')
plt.show()
