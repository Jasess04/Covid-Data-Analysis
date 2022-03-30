 Covid-Data-Analysis

This project is focused on daily reported data published by John Hopkins University for March 28th, 2022. The data was pulled from the Covid-19 Data Repository by the Center for Science and Engineering (CSSE) at John Hopkins University. The data is published as a CVS file every day. The project will be taking the raw CVS data and turning it into a bar graph that shows the top 20 countries with the most confirmed covid cases from most to least descending. 

The Plot graphic displays the top 20 countries with the maximum number of confirmed covid cases at the time the data was collected. 

The second Plot shows the top 5 countries with the maximum number of confirmed covid cases. 

Note: The Code takes a moment to compile and run. There is a brief delay before the bar plots and data appears. 
                                                                                                      
=======

Requirements

A working Python environment using Python 3.9.6 or newer

=======

Instructions

Pull the code down: git clone https://github.com/Jasess04/Covid-Data-Analysis
Enter project folder: cd Covid-Data-Analysis-main
Install required Python packages: pip install -r requirements (Please see below in the next section)
Execute: python CovidData.py

=======

Packages to Install 

import pandas as pd # pandas is being used to manipulate matplotlib and NumPy

import numpy as np # is being used for mathematical operations

import matplotlib.pyplot as plt # is used for data visualization

import seaborn as sns # the data visualization library used in conjuction with matplotlib

import plotly.express as px ### for plotting the data on world map

=======

Expectation 

A message in the terminal should inform the user that the data is populating. 

The Data will be pulled from the John Hopkins URL for 3/28/2022 and the data will be tabulated onto a BAR CHART figure showing the top 20 countries with confirmed covid cases in different colors. 

The next data chart shows the top five countries with the most confirmed covid cases at the time of the data pull. This chart will appear after the first chart is closed. 

Lastly, the program tells the user in the terminal how many days are left until the project 
needs to be turned in. 

=======

Features Implemented

Category 1: Create a class, then create at least one object of that class and populate it with data. The value of at least one object must be used somewhere in your code.

#Category 1: Calculate and display data based on an external factor (ex: get the current date, and display how many days remain until some event).

Category 2: Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program.

Category 2: Utilize External Data: Read data from an external file, such as text, JSON, CSV, etc, and use that data in your application.

Category 3: Data Display: Visualize data in a graph, chart, or other visual representation of data.

“STRETCH” FEATURE LIST: Implement a “scraper” that can be fed a type of file or URL and pull information off of it. For example, a web scraper that lets you provide any website URL and it will find certain keywords on the page.

“STRETCH” FEATURE LIST: Use pandas, matplotlib, and/or numpy to perform a data analysis project. Ingest 2 or more pieces of data, analyze that data in some manner, and display a new result to a graph, chart, or other display.

=======

Core Python Documentation References

Setting up a proper Python package: https://packaging.python.org/tutorials/packaging-projects/
