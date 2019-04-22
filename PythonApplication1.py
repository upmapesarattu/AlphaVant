
from math import radians
import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt
import alphavantage
import json
import requests
from alpha_vantage.timeseries import TimeSeries

 

 

ts = TimeSeries(key='MVG4LT5VJBPRHLGD', output_format='json')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
data.plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()

#API_URL = "https://www.alphavantage.co/query" 

#data = {
#    "function": "TIME_SERIES_DAILY",
#    "symbol": "MSFT",
#    "outputsize": "compact",
#    "datatype": "csv",
#    "apikey": "MVG4LT5VJBPRHLGD",
#    }
#response = requests.get(API_URL, params=data)
#resp = response.json()


#symbols = ['MSFT',"INTC","AMZN"]

##for symbol in symbols:
##        data = { 
##            "function": "TIME_SERIES_INTRADAY", 
##        "symbol": symbol,
##        "interval" : "60min",       
##        "datatype": "json", 
##        "apikey": "MVG4LT5VJBPRHLGD. " } 
##        response = requests.get(API_URL, data) 
##        data = response.json()
##        print(symbol)
##        a = (data['Time Series (60min)'])
##        keys = (a.keys())
##        for key in keys:
##                print(a[key]['2. high'] + " " + a[key]['5. volume'])