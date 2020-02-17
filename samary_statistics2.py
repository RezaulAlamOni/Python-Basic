import numpy as np
import pandas as ps
import pandas.io.data as pdweb
import datetime

price = pdweb.get_data_yahoo(['CVX','XOM','BP'],start=datetime.datetime(2010,1,1),end=datetime.datetime(2013,1,1))['Adj Close']
print(price.head())