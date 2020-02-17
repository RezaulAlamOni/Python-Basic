import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dfram1 = pd.read_csv('text1.txt')
dfram2 = pd.read_csv('text1.txt',header = None)
dfram3 = pd.read_table('text1.txt',sep = ',',header = None)
dfram4 = pd.read_csv('text1.txt',header = None, nrows = 2)

# dfram2.to_csv('Test_csv_create.csv')
import sys
# print(dfram2.to_csv(sys.stdout))
print(dfram2.to_csv(sys.stdout), sep = '_')
