import pandas as pd
from pandas_datareader import data 
#import pandas_datareader as data
# Any difference????
#import matplotlib.pyplot as pp



#ticker=input('Enter a stock symbol:\n>>')
ticker='MACK'
stockInfo = data.DataReader(ticker,'quandl','2017-01-01','2017-04-30')
stockFrame = pd.DataFrame(stockInfo)
stockFrame = stockFrame[['Close','Open','High','Low']].astype(float)

#stockFrame = stockFrame[['Close','Open','High','Low']]
#stockFrame['Delta']=1

#print(stockInfo.head())
#print(stockInfo.tail())



stockFrame['Delta']=stockFrame['Close']-stockFrame['Open']

##y= stockFrame['Close'].values
##v=stockFrame['Delta'].values
##x= stockFrame.index

#pp.plot(x,y)
##pp.plot(x,y,label='Close')
##pp.plot(x,y,label='Delta')
##pp.legend()
##pp.show()

stockFrame = stockFrame.resample('M').mean()
print (stockInfo)
print(stockFrame)
#print(stockFrame.info)
#print(stockFrame['Close'].values)


#print (stockFrame.info())

#print (stockFrame[['Open','Close']])
#print (stockFrame.Open)



