import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

df=pd.read_csv(r'SALE.csv')

df=df.loc[df['Order ID']!='Order ID']

df.to_csv('SALE.csv',index=False)



df=df.dropna(how='all')

df.to_csv('SALE.csv',index=False)