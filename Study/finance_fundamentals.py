import pandas as pd
import quandl

quandl.ApiConfig.api_key = '4RzrQwAs5dS-9jp8xRB2'

### Sharp Ratio
start = pd.to_datetime('2012-01-01')
end = pd.to_datetime('2020-05-04')

aapl = quandl.get('WIKI/AAPL.11', start_date=start, end_date=end)
cisco = quandl.get('WIKI/CSCO.11', start_date=start, end_date=end)
ibm = quandl.get('WIKI/IBM.11', start_date=start, end_date=end)
amzn = quandl.get('WIKI/AMZN.11', start_date=start, end_date=end)

for stock_df in (aapl, cisco, ibm, amzn) :
    stock_df['Normed Return'] = stock_df['Adj. Close'] / stock_df.iloc[0]['Adj. Close']

### Portpolio Allocation
### 30% in apple, 20% in cisco, 40% in amazon, 10% in ibm
for stock_df, allo in zip((aapl, cisco, ibm, amzn), [.3,.2,.4,.1]):
    stock_df['Allocation'] = stock_df['Normed Return'] * allo

# print(aapl.head())

for stock_df in (aapl, cisco, ibm, amzn):
    stock_df['Position Values'] = stock_df['Allocation'] * 1000000

# print(aapl.head())

all_pos_vals = [aapl['Position Values'], cisco['Position Values'], ibm['Position Values'], amzn['Position Values']]

portfolio_val = pd.concat(all_pos_vals, axis=1)
portfolio_val.columns = ['AAPL Pos', 'CISCO Pos', 'IBM Pos', 'AMZN Pos']

portfolio_val['Total Pos'] = portfolio_val.sum(axis=1)

import matplotlib.pyplot as plt

# portfolio_val['Total Pos'].plot()
# plt.title('Total Portfolio Value')
#
# portfolio_val.drop('Total Pos', axis=1).plot()

portfolio_val['Daily Return'] = portfolio_val['Total Pos'].pct_change(1)
portfolio_val['Daily Return'].mean()
portfolio_val['Daily Return'].std()

# portfolio_val['Daily Return'].plot(kind='kde', figsize=(4,5))

cumulative_return = 100 * (portfolio_val['Total Pos'][-1] / portfolio_val['Total Pos'][0] - 1)


# print(cumulative_return)
# plt.show()



### Sharp Ratio
SR = portfolio_val['Daily Return'].mean() / portfolio_val['Daily Return'].std()
print(SR)
