import pandas_datareader.data as web
import datetime

start = datetime.datetime(2015,1,1)
end = datetime.datetime(2017,1,1)

# Use the codes "iex" or "morningstar" instead.
facebook = web.DataReader('FB', 'yahoo', start, end)
print(facebook)




# from pandas_datareader.data import Options
# fb_options = Options('FB','yahoo')
#
# options_df = fb_options.get_options_data(expiry=fb_options.expiry_dates[0])
# print(options_df)




