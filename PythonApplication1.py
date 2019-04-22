 
import matplotlib.pyplot as plot  #Custom Package
from alpha_vantage.timeseries import TimeSeries #Custom Package
import pandas  #Custom Package

 

 
#Intraday Chart

ts = TimeSeries(key='MVG4LT5VJBPRHLGD', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='5min', outputsize='full')
data['4. close'].plot()
 
plot.title('Intraday Times Series for the MSFT stock (1 min)')
plot.show()


#Daily Chart (Work in Progress, plot not pretty)
#ts = TimeSeries(key='MVG4LT5VJBPRHLGD', output_format='pandas')
#data, meta_data = ts.get_daily(symbol='MSFT', outputsize='full')

#data['4. close'].plot()
 
#plot.title('Daily Times Series for the MSFT stock')
#plot.show()


