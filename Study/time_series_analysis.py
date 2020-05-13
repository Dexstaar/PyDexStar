import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# df = sm.datasets.macrodata.load_pandas().data
# index = pd.Index(sm.tsa.datetools.dates_from_range('1959Q1', '2009Q3'))
# df.index = index
#
# # print(df.head())
#
# df['realgdp'].plot()
#
# gdp_cycle, gdp_trend = sm.tsa.filters.hpfilter(df['realgdp'])
# df['trend'] = gdp_trend
# df[['realgdp', 'trend']]["2000-03-31":].plot()

# plt.show()


### ETS(Error-Trend-Seasonality) Models
### EWMA (Exponentially-weighted moving average)
# airline = pd.read_csv('./Python-for-Finance-Repo-master/08-Time-Series-Analysis/airline_passengers.csv', index_col="Month")
# airline.dropna(inplace=True)
# airline.index = pd.to_datetime(airline.index)
#
# # airline['6-month-SMA'] = airline['Thousands of Passengers'].rolling(window=6).mean()
# # airline['12-month-SMA'] = airline['Thousands of Passengers'].rolling(window=12).mean()
#
# airline.plot(figsize=(10,6))
#
# airline['EWMA-12'] = airline['Thousands of Passengers'].ewm(span=12).mean()
# airline[['Thousands of Passengers', 'EWMA-12']].plot(figsize=(10,6))
#
# plt.show()


### ETS Decomposition Code Along

# airline = pd.read_csv('./Python-for-Finance-Repo-master/08-Time-Series-Analysis/airline_passengers.csv', index_col="Month")
# # airline.plot()
# airline.dropna(inplace=True)
# airline.index = pd.to_datetime(airline.index)
#
# from statsmodels.tsa.seasonal import seasonal_decompose
# result = seasonal_decompose(airline['Thousands of Passengers'], model='multiplicative')
# result.plot()
#
# plt.show()


### ARIMA(Auto Regressive Integrated Moving Average, 자가회귀누적이동평) models
df = pd.read_csv('./Python-for-Finance-Repo-master/08-Time-Series-Analysis/monthly-milk-production-pounds-p.csv')
df.drop(168, axis=0, inplace=True)
df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month', inplace=True)
#print(df.describe().transpose())

df.plot()
plt.show()
