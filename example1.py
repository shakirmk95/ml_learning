#Regression
import pandas as pd
import quandl
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

df = quandl.get('WIKI/GOOGL')

print(df.head())
