#PyData Seattle 2017; youtube tutorial; https://www.youtube.com/watch?v=5XGycFIe8qE
import pandas as pd

data = pd.read_csv('coffees.csv')

#check few data sets
data.head()

print("Dataset length:")
print(len(data))

#Find null datasets on coffees
data[data.coffees.isnull()]

#whats the datatype in all columns
data.dtypes

#timestamp column, whats the datatype
print(type(data.timestamp[0]))

##CSV imports as strings
## To Fix: (1) coffees as string & null (2) datetimes is shown as string

# (1) cast coffee column as pd.to_numeric and coerce errors
data.coffees = pd.to_numeric(data.coffees, errors="coerce")     #coerce converts errors into NaN

#drop NA from the dataframe
data.dropna()       #this operates on copies- still shows them
data.dropna(inplace=True)       #actually drops the NA
data = data.dropna()            #another implementations

#convert coffeees to integers
data.coffees = data.coffees.astype(int)

# (2) convert the timestamp to appropriate type
data.timestamp = pd.to_datetime(data.timestamp)         #normally, convert to numeric first, then dates- incase of errors

#lets check out the data
data.describe()     #when dataframe is mixed, pandas defaults to numeric
data.describe(incude="all")     #gimme all the datas

#plot the coffee series
data.coffees.plot()
plt.show()      #its plottng by index instead of timestam[ == wrong!

data.plot(x='timestamp', style=".-"); plt.show()

#the tail data looks not useful; get rid of everything after March
data.timestamp < '2013-03-01'
data[data.timestamp < "2013-03-01"].tail()

data = data[data.timestamp < "2013-03-01"]
data.plot(x='timestamp' style=".-", figsize=(15,4)); plt.show()

## Lets look at contributors
data.contributor.value_counts()
data.contributor.value_counts().plot(kind="bar")

## Lets look at activity days
weekdays = data.timestamp.dt.weekday        #because timestamp series is dates, we can use 'dt' property
data = data.assign(weekdays=weekdays)       #create a new column that assigns date to weekday integer value

# now replace weekday integers to string
weekday_names = ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday', 'Sat','Sun']
weekday_dict = {key: weekday_names[key] for key in range(7)}

def day_of_week(idx):           #function to take integer input & outputs day of week
    return weekday_dict[idx]

day_of_week(0)

# now we go into dataframe and call the integers as inputs to newly created function then save results onto of it
data.weekdays = data.weekdays.apply(day_of_week)
data.head()

## Group by weekdays; you can use .values_counts() or .groupby()
weekday_counts = data.groupby("weekdays")       #you can always integrate step below by adding .count()
weekday_counts = weekday_counts.count()         #count the groupings
weekday_counts

#Lets sort the data by an ordered list
weekday_counts = weekday_counts.loc[weekday_names]
weekday_counts

#Visualize data
weekday_counts.coffees.plot(kind='bar'); plt.show()

# convert index to timestamp- why? dataframe cant exist w/o index (index is auto created)
data.index = data.timestamp

#drop repeating timestamp column
data.drop('timestamp'], axis=1, inplace=True)           #axis=1 drops column, usually it works on rows but we wanted to drop column
data.head()

# to find coffees per 1 day; we create a row "midnight" each day, then count all coffees for that day & add into "midnight"
midnights = pd.date_range(data.index[0], data.index[-1], freq="D", normalize=True)
midnights

#we have 2 dataframes- midnights & data.index, wherein one is evenly spaced (midnights) and the other is not.
# Lets take the union of these indexes
 new_index = midnights.union(data.index)        #come up w/ new index that has 2 both in 1 index & sorted in order

 #reindex our dataframe
 upsampled_data = data.reindex(new_index)

 upsampled_data.head(10)

#We fill NaNs using interpolation
upsampled_data = upsampled_data.interpolate(method="time")
upsampled_data.head(10)

 #Now lets resamplet the data on daily frequency
daily_data = upsampled_data.resample("D").asfreq()

#drop contributor column, useless NaN
daily_data = daily_data.drop(['contributor'], axis=1)
daily_data['weekdays'] = daily_data.index.weekdays_name     #there's built-in method to get days of week; instead of dictionary hack done before

#Lets plot data again!
daily_data.plot(); plt.show()

# how many coffees were made?  remember the raw data is running sum of coffees made with timestamps
coffees_made = daily_data.coffees.diff()
coffess_made = daily_data.coffeses.diff().shift(-1)     #we want coffees made to be attributed to day of, not after
coffees_made

# add the data into main dataframe
daily_data["coffees_made_today"] = coffees_made


# how many coffees by day
coffee_by_day = daily_data.groupby("weekdays").mean()
coffees_by_day      #now its getting insightful; average coffee made on sunday is 12, monday 42...&etc

#sort the weekdays in order
coffees_by_day = coffees_by_day.loc[weekday_names]
coffees_by_day.coffees_made_today.plot(kind="bar"); plt.show()
