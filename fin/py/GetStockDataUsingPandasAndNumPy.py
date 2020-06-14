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

START_DATE = '2005-01-01'
END_DATE = str(datetime.now().strftime('%Y-%m-%d')) # Today

STOCK = 'MS'

def get_data(ticker):
    try:
        stock_data = data.DataReader(ticker, 'yahoo', START_DATE, END_DATE)
        print(stock_data)
    except RemoteDataError:
        print('No data found for {t}'.format(t=ticker))

get_data(STOCK)