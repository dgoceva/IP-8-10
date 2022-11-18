import csv
import matplotlib.pyplot as plt
from datetime import datetime

FNAME = '3139529.csv'

with open(FNAME) as f:
    reader = csv.reader(f)
    header = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        # try:
        if row[5] != '' and row[6] != '':
            highs.append(float(row[5]))
            lows.append(float(row[6]))
            dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
        # except ValueError:
        #     print(f'Missing high temperature for {row[2]}')

# print(header)
# print(highs)

# plt.style.use('seaborn')
# plt.style.use('ggplot')
fig, ax = plt.subplots()
fig.autofmt_xdate()
ax.tick_params(axis='both', labelsize=14)
ax.set_title('Daily High Temperature\nSofia, 2022', fontsize=20)
ax.set_xlabel('Date', fontsize=16)
ax.set_ylabel('Temperature (C)', fontsize=16)
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, lows, highs, color='blue', alpha=0.1)
plt.show()
