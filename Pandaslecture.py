import pandas as pd
from pandas_datareader import data 

ticker='MACK'
stockInfo = data.DataReader(ticker,'quandl','2017-01-01','2017-04-30')
stockFrame = pd.DataFrame(stockInfo)
stockFrame = stockFrame[['Close','Open','High','Low']].astype(float)

#pp.plot(x,y)
##pp.plot(x,y,label='Close')
##pp.plot(x,y,label='Delta')
##pp.legend()
##pp.show()

stockFrame = stockFrame.resample('M').mean()
print (stockInfo)
print(stockFrame)




