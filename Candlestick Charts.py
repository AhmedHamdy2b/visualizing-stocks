import datetime as dt
import pandas_datareader.data as web
import mplfinance as mpf


start = dt.datetime(2019, 1, 1)
end = dt.datetime.now()

data = web.DataReader('FB', 'yahoo', start, end)

mpf.plot(data, type="candle")