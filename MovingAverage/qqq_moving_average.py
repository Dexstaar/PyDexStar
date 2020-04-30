import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

company = web.DataReader("QQQ", "yahoo", "2019-11-01", "2020-04-29")
company_wd = company[company['Volume'] != 0]

# 90일 이동평균값
ma90 = company_wd['Adj Close'].rolling(window=90).mean()

# 이동평균값을 데이터셋에 추가
company_wd.insert(len(company_wd.columns), "MA90", ma90)

# print(company_wd)

# 주간이동평균선 그리기
plt.plot(company_wd.index, company_wd['Adj Close'], label="Adj Close")
plt.plot(company_wd.index, company_wd['MA90'], label="MA90")

plt.legend(loc='best')
plt.grid()
plt.show()

