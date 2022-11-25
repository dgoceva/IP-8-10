import pandas as pd
import matplotlib.pyplot as plt

FNAME = '3139529.csv'

data = pd.read_csv(FNAME).dropna()
# print(data)

data.plot(title='Daily High Temperature\nSofia, 2022',
          xlabel='Date', ylabel='Temperature, C',
          x='DATE', y=['TMIN', 'TMAX'], rot=15, color=['blue', 'red'], alpha=0.5)
plt.fill_between(data['DATE'], data['TMIN'], data['TMAX'], alpha=0.1)
plt.show()
