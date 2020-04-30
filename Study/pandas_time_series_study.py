import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

my_year = 2017
my_month = 1
my_day = 2
my_hour = 13
my_minute = 30
my_second = 15

my_date = datetime(my_year, my_month, my_day)
my_date_time = datetime(my_year, my_month, my_day, my_hour, my_minute, my_second)

first_two = [datetime(2016,1,1), datetime(2016,1,2)]
dt_ind = pd.DatetimeIndex(first_two)

print(dt_ind)

