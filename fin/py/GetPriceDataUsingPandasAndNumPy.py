# Dependencies
# 1. pip insall pandas-datareader
# 2. pip install matplotlib
# 3. pip install pandas
# 4. pip install numpy
# 5. pip install datetime

# Troubleshooting
# 1. Ctrl + Shift + P to change the Python Interpreter
# 2. python -m pip install --upgrade pip

from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

START_DATE = '2015-01-01'
END_DATE = str(datetime.now().strftime('%Y-%m-%d')) # Today
# print(START_DATE)
# print(END_DATE)

SYMBOL = 'SPY'

def get_stats(price_data):
    return {
        'last': np.mean(price_data.tail(1)),
        'fast_period': np.mean(price_data.tail(50)),
        'slow_period': np.mean(price_data.tail(200)),
        'fast_sma': price_data.rolling(window=50).mean(),
        'slow_sma': price_data.rolling(window=200).mean()
    }

def clean_data(price_data, col):
    weekdays = pd.date_range(start=START_DATE, end=END_DATE)
    clean_data = price_data[col].reindex(weekdays)
    return clean_data.fillna(method='ffill')

def create_plot(price_data, symbol):
    stats = get_stats(price_data)
    # plt.style.use('dark_background')
    plt.subplots(figsize=(12,8))
    plt.plot(price_data, label=symbol)
    plt.plot(stats['fast_sma'], label='SMA(50)')
    plt.plot(stats['slow_sma'], label='SMA(200)')
    plt.xlabel('Date')
    plt.ylabel('Adj Close')
    plt.legend()
    plt.title('Daily')
    plt.show()

def get_data(symbol):
    try:
        # Google Data
        # Google has changed the Google Finance URL to finance.google.com/finance/historical
        #  rather than www.google.com/finance/historical, which is used as the URL in the 
        # pandas_datareader. Server returns HTTP 302 when fetching data from the old URL 
        # and redirect to the new URL. However, the parameters startdate/enddate are missing 
        # during the HTTP redirection.
        
        # IEX Data
        # The  Cloud API key must be provided either through the api_key 
        #   variable or through the  environment variable IEX_API_KEY
        # price_data = data.DataReader(symbol, 'iex', START_DATE, END_DATE)

        # Yahoo Data
        price_data = data.DataReader(symbol, 'yahoo', START_DATE, END_DATE)
        # print(price_data.head)
        # print(price_data)
        
        # print(clean_data(price_data, 'Adj Close'))

        adj_close = clean_data(price_data, 'Adj Close')

        create_plot(adj_close, symbol)

    except RemoteDataError:
        print('No data found for {s}'.format(s=symbol))

get_data(SYMBOL)