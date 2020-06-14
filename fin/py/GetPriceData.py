import pandas as pd
import pandas_datareader.data as web
import datetime as dt
from datetime import datetime
import os

def get_stock_data():
    tickers = ['SPY', 'DIA', 'QQQ']

    start = dt.datetime(2019,1,1)
    end = dt.datetime.today()

    if not os.path.exists('stockdata'):
        os.makedirs('stockdata')

    for ticker in tickers:
        print(ticker)
        try:
            df = web.DataReader(ticker, "iex", start, end)
            print(df.head())
            df.to_csv('stockdata/{}.csv', format(ticker))
            print(ticker, 'downloaded')
        except Exception as e:
            print(e, 'error')

get_stock_data()