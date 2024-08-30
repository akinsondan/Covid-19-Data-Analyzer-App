import numpy as np
import os
import pandas as pd
from string import punctuation

# initial data cleaning

# load file in covid_data
covid19_data = pd.read_csv('COVID-19_Cases_World.csv')

# check for null values
print(covid19_data.isna())

# check cases column for negative value
print(covid19_data.loc[covid19_data.cases < 0])

# check deaths column for negative value
print(covid19_data.loc[covid19_data.deaths < 0])

# remove negatives from both columns
covid19_data.cases = covid19_data.cases.abs()
covid19_data.deaths = covid19_data.deaths.abs()

# create dict to rename values in month column
month_dict = {1:'January', 2: 'February', 3:'March', 4:'April', 5:'May', 6:'June',
              7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

# replace values in month column
covid19_data.month = covid19_data.month.map(month_dict)

# drop null values
covid19_data.dropna(inplace=True)

# check for punctuations in DF
print(covid19_data.isin(list(punctuation)).any().any())

# save cleaned data to current working directory
cwd = os.getcwd()
path = cwd + "/cleaned_covid19_data.csv"
covid19_data.to_csv(path,index=False)