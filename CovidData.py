import pandas as pd #pandas is being used to manipulate matplotlib and NumPy
import numpy as np #is being used for mathematical operations
import matplotlib.pyplot as plt #is used for data visualization
import seaborn as sns #the data visualization library used in conjuction with matplotlib



# the raw CVS data from John Hopkins University's daily Covid-19 reports during the 02-11-2022 timeframe
path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/02-11-2022.csv'
df = pd.read_csv(path)
df.info()
df.head()

# Removes data concerning 'FIPS', 'Admin2','Last_Update' since all the data focuses on a 02-11-2022 
# Removing columns ‘Province_State’ and ‘Combined_Key’ since statewide data is not available for all the countries.
df.drop(['FIPS', 'Admin2','Last_Update','Province_State', 'Combined_Key'], axis=1, inplace=True)
df.rename(columns={'Country_Region': "Country"}, inplace=True) #shortens 'country_region' to just 'country'
df.head()

                                ### group the data by country ###

# All data is correlated together with the dataframe 'groupby'
world = df.groupby("Country")['Confirmed','Active','Recovered','Deaths'].sum().reset_index()
world.head()

# Find top 20 countries with maximum number of confirmed cases
top_20 = world.sort_values(by=['Confirmed'], ascending=False).head(20)
plt.figure(figsize=(12,10))
plot = sns.barplot(top_20['Confirmed'], top_20['Country'])

for i,(value,name) in enumerate(zip(top_20['Confirmed'],top_20['Country'])):
  plot.text(value,i-0.05,f'{value:,.0f}',size=10)
plt.show()
