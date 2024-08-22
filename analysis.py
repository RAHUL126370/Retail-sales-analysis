import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import datetime

df=pd.read_csv(r'SALE.csv')

df['Order Date']=pd.to_datetime(df['Order Date'])

df['Order Month']=df['Order Date'].dt.month
df['Order Month name']=df['Order Date'].dt.month_name()

df.to_csv('SALE.csv',index=False)