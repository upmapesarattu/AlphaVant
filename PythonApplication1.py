
from math import radians
import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt
import alphavantage
import json
import requests
from alpha_vantage.timeseries import TimeSeries
import pandas

 

 
#Intraday Chart

ts = TimeSeries(key='MVG4LT5VJBPRHLGD', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='5min', outputsize='full')
data['4. close'].plot()
 
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()


#Daily Chart
#ts = TimeSeries(key='MVG4LT5VJBPRHLGD', output_format='pandas')
#data, meta_data = ts.get_daily(symbol='MSFT', outputsize='full')

#data['4. close'].plot()
 
#plt.title('Daily Times Series for the MSFT stock')
#plt.show()


