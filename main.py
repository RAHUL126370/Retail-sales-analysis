import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

edf = pd.DataFrame()
filenames = os.listdir('SalesData')

for filename in filenames:
    df = pd.read_csv(f'SalesData/{filename}')

    edf = pd.concat([df, edf])

    edf.to_csv('SALE.csv', index=False)