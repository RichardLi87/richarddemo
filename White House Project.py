import matplotlib as mpl
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter
import csv
import datetime

df = pd.read_csv('white_house_statement.csv')
df.head(5)

filt_Trump = df['Title'].str.contains('Trump')
filt_2017 = (df['Date'] >= '2017-01-01') & (df['Date']< '2018-01-01')
filt_2018 = (df['Date'] >= '2018-01-01') & (df['Date']< '2019-01-01')
filt_2019 = (df['Date'] >= '2019-01-01') & (df['Date']< '2020-01-01')
filt_2020 = (df['Date'] >= '2020-01-01') & (df['Date']< '2021-01-01')

plt.style.use('seaborn')

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()

ax1.barh(department_2020, amount_2020)
ret_2020 = ax1.barh(department_2020, amount_2020, color='grey')
ret_2020[0].set_color('r')
ret_2020[1].set_color('r')
ret_2020[6].set_color('b')
ret_2020[9].set_color('b')
ret_2020[11].set_color('b')
ret_2020[12].set_color('b')

ax2.barh(department_2019,amount_2019)
ret_2019 = ax2.barh(department_2019,amount_2019,color = 'grey')
ret_2019[0].set_color('r')
ret_2019[1].set_color('r')
ret_2019[6].set_color('b')
ret_2019[9].set_color('b')
ret_2019[10].set_color('b')
ret_2019[12].set_color('b')