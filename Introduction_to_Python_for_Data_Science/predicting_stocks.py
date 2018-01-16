#stock price analysis
import pandas as pd

data = pd.read_csv('AAPL.csv')            #file has headers, no need to set them
dates = []
prices = []

data.Date = pd.to_datetime(data.Date)
data.plot(x='Date',y='Open',style=".-"); plt.show()

#linear regresssion;
reg = linear_model.LinearRegression()
reg.fit(data.Date, data.Open)

data.plot(x='Date',y='Open',style=".-"); plt.show()
