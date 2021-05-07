## Anissa Champion
## Final Project
## Amazon spending 
##05/02/2020
## This is just the code , I created this with jupyter notebook which is cell by cell so this 
##formatting may be different 
import pandas as pd

df1 = pd.read_csv('2020amazonspending.csv')
df1.head()
df2= pd.read_csv('2021amazonreport.csv')
df2.head()
##getting the shape
df1.shape 
df2.shape
df1 = df.fillna(0)
df1.head()
## Cleaning data for 2021 report
df2 = df2.fillna(0)
df2.head()
##before I am able to do calculation I have to remove $ signs
df1["Item Total"] = df1["Item Total"].str.replace('$','').astype(float)
df1.head()
##before I am able to do calculation I have to remove $ signs
df2["Item Total"] = df2["Item Total"].str.replace('$','').astype(float)
df2.head()
sum = df1["Item Total"].sum()
print("2020 total is ", sum)
sum2 = df2["Item Total"].sum()
print("2021 total is ", sum2)
sumtotal = sum+sum2
print ("During the pandemic I have Spent" ,sumtotal, "dollars on Amazon ")
mean= df1["Item Total"].mean()
print("2020 mean is  ", mean)
mean2= df2["Item Total"].mean()
print("2021 mean is  ", mean2)
df1['Order Date'] = pd.to_datetime(df1['Order Date'])
df1.head()
df2['Order Date'] = pd.to_datetime(df2['Order Date'])
df2.head()
plot= df1.plot.bar(x='Order Date', y='Item Total', rot=90, figsize=(20,10))
print(plot)
plot= df2.plot.bar(x='Order Date', y='Item Total', rot=90, figsize=(20,10))
print(plot)