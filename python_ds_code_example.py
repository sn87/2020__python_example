#!/usr/bin/env python
# coding: utf-8
# inspired by: https://www.developintelligence.com/blog/2017/08/plotting-climate-data-matplotlib-python/
# dataset: https://www.ncdc.noaa.gov/cag/time-series/global/globe/land_ocean/1/6/1880-2017.csv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('1880-2017.csv', header = 4)
df.head()

def get_mean():
# Get mean value
    print(df['Value'].mean())

get_mean()

def get_median():
# Get median value
    print(df['Value'].median())

get_median()
    
def get_val_by_year(year):
# Get value by year
    print(df.loc[df['Year'] == year, 'Value'].iloc[0])

get_val_by_year(1880)

# Create bar plot
plt.bar(df['Year'], df['Value'], color ='blue') 
plt.xlabel("Year") 
plt.ylabel("Fahrenheit deviation from average") 
plt.title("Global Temperature Anomalies (June)") 
plt.show() 
