import pandas as pd # pandas is being used to manipulate matplotlib and NumPy
import numpy as np # is being used for mathematical operations
import matplotlib.pyplot as plt # is used for data visualization
import seaborn as sns # the data visualization library used in conjuction with matplotlib
import plotly.express as px ### for plotting the data on world mapfrom datetime import datetime
from datetime import datetime

# Category Stretch Goal: Pull data from URL
# the raw CVS data from John Hopkins University's daily Covid-19 reports during the 03-06-2022 timeframe
path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-06-2022.csv'
df = pd.read_csv(path)
df.info()
df.head()

# Category 1: Create a class
# Removes data concerning 'FIPS', 'Admin2','Last_Update' since all the data focuses on a 03-06-2022 
# Cleaning the data by removing columns ‘Province_State’ and ‘Combined_Key’ since statewide data is not available for all the countries.

df.drop(['FIPS', 'Admin2','Last_Update','Province_State', 'Combined_Key'], axis=1, inplace=True)
df.rename(columns={'Country_Region': "Country"}, inplace=True) #shortens 'country_region' to just 'country'
df.head()

                             ### group the data by country ###

# Category 2: A list
# All data is correlated together with the dataframe 'groupby'

world = df.groupby("Country")['Confirmed','Active','Recovered','Deaths'].sum().reset_index()
world.head()

# Category 3: Data Display
# Category 2: Create a dictionary or list
# Find top 20 countries with maximum number of confirmed cases

top_20 = world.sort_values(by=['Confirmed'], ascending=False).head(20)
plt.figure(figsize=(12,10))
plot = sns.barplot(top_20['Confirmed'], top_20['Country'])

for i,(value,name) in enumerate(zip(top_20['Confirmed'],top_20['Country'])):
  plot.text(value,i-0.05,f'{value:,.0f}',size=10)
plt.show()

# Category 3: Data Display
#  The top five Countries with the maximum number of confirmed cases
top_5 = world.sort_values(by=['Confirmed'], ascending=False).head()

#  Generate a Barplot
plt.figure(figsize=(15,5))
confirmed = sns.barplot(top_5['Confirmed'], top_5['Country'], color = 'red', label='Confirmed')

# Adding Texts for barplots
for i,(value,name) in enumerate(zip(top_5['Confirmed'],top_5['Country'])):
  confirmed.text(value,i-0.05,f'{value:,.0f}',size=9)
plt.legend(loc=4)
plt.show()

# Category 3: Data Display
# Creates a world map depicting where the highest confirmed covid cases are based on color. 
figure = px.choropleth(world, locations='Country', locationmode='Country names', color='Confirmed', hover_name='Country', color_continuous_scale='tealgrn', range_color=[1,1000000],title='Countries with Confirmed cases')
figure.show()

