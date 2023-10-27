import requests
import re
import pygal
from datetime import datetime
import pandas as pd
import csv
import json

key = "M2JJMD2LF2NOSOOH"
print("Stock Data Visualizer")
print("__________________________")

def get_Symbol():
    global userSymbol 
    userSymbol = input("Enter the stock symbol you are looking for: ")
    print("")
    #if (userSymbol == "GOOGL"):
    #    print("Works")
    #else:
    #    print("Doesn't Work")

def get_Time():
    global timeSeries
    print("Select the Time Series of the chart you want to Generate ")
    print("________________________________________________________________")
    print("1. Intraday")
    print("2. Daily")
    print("3. Weekly")
    print("4. Monthly")

    userTime = input("Enter time series option (1, 2, 3, 4): ")
    if (userTime == "1"):
        timeSeries = "TIME_SERIES_INTRADAY"
        #print (timeSeries)
    elif (userTime == "2"):
        timeSeries = "TIME_SERIES_DAILY"
        #print (timeSeries)
    elif (userTime == "3"):
        timeSeries = "TIME_SERIES_WEEKLY"
        #print (timeSeries)
    elif (userTime == "4"):
        timeSeries = "TIME_SERIES_MONTHLY"
        #print (timeSeries)
    else:
        print(" ")
        print("Please be sure to input 1, 2, 3, or 4. Try again.")
        print(" ")
        get_Time()

def get_Start():
    global start_date
    while True:
        print("Please input the start date of the data you'd like. (YYYY-MM-DD)")
        user_start = input("Enter Date: ")
    
        date_pattern = r'^\d{4}-\d{2}-\d{2}$'

        if(re.match(date_pattern, user_start)):
            start_date = user_start
            break
        else:
            print("Invalid date, please use YYYY-MM-DD format.")

def get_End():
    global end_date
    while True:
        print("Please input the end date of the data you'd like. (YYYY-MM-DD)")
        user_end = input("Enter Date: ")
    
        date_pattern = r'^\d{4}-\d{2}-\d{2}$'

        if(re.match(date_pattern, user_end)):
            date1_obj = datetime.strptime(start_date, "%Y-%m-%d")
            date2_obj = datetime.strptime(user_end, "%Y-%m-%d")
        if(date1_obj <= date2_obj):
            end_date = user_end
            break
        else:
                print("End date must come after the start date.")
    else:
        print("Invalid date, please use YYYY-MM-DD format.")
        


def get_ChartType():
    global chartType
    print("Select the type of chart you want to Generate ")
    print("________________________________________________________________")
    print("1. Line Chart")
    print("2. Bar Chart")

    userChartType = input("Enter chart type option (1 or 2): ")
    if userChartType == "1":
        chartType = "line"
    elif userChartType == "2":
        chartType = "bar"
    else:
        print(" ")
        print("Please be sure to input 1, or 2. Try again.")
        print(" ")
        get_ChartType()

#def generate_and_show_chart():
#    if chartType == "line":
#        line_chart = pygal.Line()
#        line_chart.title = 'Browser usage evolution (in %)'
#        line_chart.x_labels = map(str, range(2002, 2013))
#        line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
#        line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
#        line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
#        line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
#        line_chart.render()


def getData():
    url = 'https://www.alphavantage.co/query?function='+ timeSeries + '&symbol=' + userSymbol + '&interval=5min&apikey=' + key #+ '&datatype=csv'
    r = requests.get(url)
    data = r.json()
    print(data)
    
def main():
    get_Symbol()
    get_Time()
    get_ChartType()
    get_Start()
    get_End()
    getData()
#    generate_and_show_chart()

main()
