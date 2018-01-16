#statistics in python
## http://www.scipy-lectures.org/packages/statistics/index.html

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("brain_size.csv", sep=";", na_values=".")
print(data.dtypes)
print(data.head())

print(data.shape)
print(data.columns)
print(data['Gender'])
print(data[data['Gender'] == 'Female']['VIQ'].mean())

#groupby
groupby_gender = data.groupby('Gender')
for gender, value in groupby_gender['VIQ']:
    print((gender, value.mean()))

print(groupby_gender['VIQ'].mean())

### <--- Exercises -->
#1 What is the mean value for the VIQ for the full population
print(data.VIQ.mean())

#2 How many males/females were included in this study?
print(groupby_gender.Gender.count())
for gender, value in groupby_gender.Gender:
    print(gender, value.count())

#3 what is the average valueof MRI counts expressed in log units, for males and females?
for gender, value in groupby_gender.MRI_Count:
    print((gender, np.log(value.mean())))

groupby_gender.MRI_Count.mean()
## boxplots
groupby_gender.boxplot(column=['FSIQ','VIQ','PIQ'])
plt.show()
data.boxplot(column=['FSIQ','VIQ','PIQ'], by='Gender'); plt.show()

## Plotting data
from pandas import plotting
plotting.scatter_matrix(data[['Weight','Height','MRI_Count']]); plt.show()

## <-- Exercise -->
#1 plot scatter matrix for males only; females only
data_male = data[data.Gender=='Male']
data_femae=data[data.Gender=='Female']
plotting.scatter_matrix(data_male[['Weight','Height','MRI_Count']])
plotting.scatter_matrix(data_female[['Weight','Height','MRI_Count']])
plt.show()

# Kernel density estimates
data.Weight.hist(normed=True); data.Weight.plot(kind='kde', grid=True); plt.show()


####<-- Linear regression --> #####
