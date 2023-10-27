import requests
import re
from datetime import datetime

key = "QNBSQ569PDAHAV41"
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
        print("Please input the start date of the data you'd like. (YYYY-MM-DD)")
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
    print("3. Candlestick Chart")

    userChartType = input("Enter chart type option (1, 2, 3): ")
    if userChartType == "1":
        chartType = "line"
    elif userChartType == "2":
        chartType = "bar"
    elif userChartType == "3":
        chartType = "candlestick"
    else:
        print(" ")
        print("Please be sure to input 1, 2, or 3. Try again.")
        print(" ")
        get_ChartType()

def generate_and_show_chart(data):
    if chartType == "line":
        x = list(data["Time Series (1min)"].keys())
        y = [float(data["Time Series (1min)"][key]["1. open"]) for key in x]
        
        plt.plot(x, y)
        plt.xlabel("Time")
        plt.ylabel("Open Price")
        plt.title("Stock Price Line Chart")
        plt.xticks(rotation=45)
        plt.tight_layout()

        chart_file = "stock_chart.png"
        plt.savefig(chart_file)
        
        plt.show()

def getData():
    url = 'https://www.alphavantage.co/query?function='+ timeSeries + '&symbol=' + userSymbol + '&interval=5min&apikey=' + key
    r = requests.get(url)
    data = r.json()
    print(data)
    
def main():
    get_Symbol()
    get_Time()
    get_ChartType()
    data = getData()
    generate_and_show_chart(data)


if __name__ == "__main__":
    main()
 
