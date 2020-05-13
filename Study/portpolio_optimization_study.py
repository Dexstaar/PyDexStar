import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

aapl = pd.read_csv('./Python-for-Finance-Repo-master/09-Python-Finance-Fundamentals/AAPL_CLOSE', index_col='Date', parse_dates=True)
cisco = pd.read_csv('./Python-for-Finance-Repo-master/09-Python-Finance-Fundamentals/CISCO_CLOSE', index_col='Date', parse_dates=True)
ibm = pd.read_csv('./Python-for-Finance-Repo-master/09-Python-Finance-Fundamentals/IBM_CLOSE', index_col='Date', parse_dates=True)
amzn = pd.read_csv('./Python-for-Finance-Repo-master/09-Python-Finance-Fundamentals/AMZN_CLOSE', index_col='Date', parse_dates=True)

stocks = pd.concat([aapl, cisco, ibm, amzn], axis=1)
stocks.columns = ['aapl', 'cisco', 'ibm', 'amzn']

stocks.pct_change(1).mean()
stocks.pct_change(1).corr()

log_ret = np.log(stocks/stocks.shift(1))
log_ret.hist(bins=100)

plt.tight_layout()

log_ret.mean()
log_ret.cov()* 252

np.random.seed(101)
# print(stocks.columns)

### Weights
weights = np.array(np.random.random(4))

# print("Random Weights:")
# print(weights)
#
# print('Rebalance')
weights = weights/np.sum(weights)
# print(weights)

### Expected Return
# print('Expected Portfolio Return')
exp_ret = np.sum( (log_ret.mean() * weights) * 252)
# print(exp_ret)

## Expected Volatility
# print('Expected Volatility')
exp_vol = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov()*252, weights)))
# print(exp_vol)

### Sharpe Ratio
# print('Sharpe Ratio')
SR = exp_ret / exp_vol
# print(SR)



