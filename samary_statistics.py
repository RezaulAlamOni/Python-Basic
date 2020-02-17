import numpy as np
from pandas import Series, DataFrame
import pandas as ps

arr = np.array([[1,2,np.nan],[np.nan,3,4]])

datafram1 = DataFrame(arr,index=['A',"B"],columns=['one','two','three'])
# datafram1.sum()
# print(datafram1.sum())
# print(datafram1.sum(axis=1))
# print(datafram1.min())
# print(datafram1.idxmin())
# print(datafram1.cumsum())
# print(datafram1.describe())
from IPython.display import YouTubeVideo
YouTubeVideo('8H93QYs7rvs')
