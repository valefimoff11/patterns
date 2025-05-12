import pandas as pd
import numpy as np

print(pd.Timestamp(year=1982, month=9, day=4, hour=1, minute=35, second=10))
print(pd.Timestamp('1982-09-04 1:35.18'))
print(pd.Timestamp('Sep 04, 1982 1:35.18'))

print(pd.Timestamp(5000))

time_stamp = pd.Timestamp('2022-02-09')
print('{}, {} {}, {}'.format(time_stamp.day_name(), time_stamp.month_name(), time_stamp.day, time_stamp.year))

year = pd.Period('2021')
print(year)

print('Start Time:', year.start_time)
print('End Time:', year.end_time)

month = pd.Period('2022-01')
print(month)
print('Start Time:', month.start_time)
print('End Time:', month.end_time)

day = pd.Period('2022-01', freq='D')
print(day)
print('Start Time:', day.start_time)
print('End Time:', day.end_time)

hour = pd.Period('2022-02-09 16:00:00', freq='H')
print(hour)
print(hour + 2)
print(hour - 2)

print(hour + pd.offsets.Hour(+2))
print(hour + pd.offsets.Hour(-2))

print(hour + pd.offsets.Hour(+2))
print(hour + pd.offsets.Hour(-2))

week = pd.date_range('2022-2-7', periods=7)
for day in week:
    print('{}-{}\t{}'.format(day.day_of_week, day.day_name(), day.date()))

df = pd.read_csv('E:\\pyprojects\\patterns\\patterns\\sampledata\\server_util.csv')
print(df.head())

print(df.info())

df['datetime'] = pd.to_datetime(df['datetime'])

print(df.info())

df = pd.read_csv('E:\\pyprojects\\patterns\\patterns\\sampledata\\server_util.csv', parse_dates=['datetime'])
print(df.head())

print(df.datetime.min())
print(df.datetime.max())

mask = (df.datetime >= pd.Timestamp('2019-03-06')) & (df.datetime < pd.Timestamp('2019-03-07'))
print(df.loc[mask])

df.set_index('datetime', inplace=True)
print(df)

print(df.loc['2019-03-07 02:00:00'].head(5))
print(df.loc['2019-03-07'].head(5))

df.loc['Apr 2019']
df.loc['8th April 2019']
df.loc['April 05, 2019 5pm']

#print(df.loc['03-04-2019':'04-04-2019'])
print(df.sort_index().loc['03-04-2019':'04-04-2019'])

print(type(df.index))
print(df.at_time('09:00'))

print(df.between_time('00:00','02:00'))

print(df.sort_index().first('5B'))

print(df.sort_index().last('1W'))

df.sort_index().last('2W')

df[df.server_id == 100].resample('D')['cpu_utilization', 'free_memory', 'session_count'].mean()

df.groupby(df.server_id).resample('M')['cpu_utilization', 'free_memory'].max()

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(24, 8))
df.groupby(df.server_id).resample('M')['cpu_utilization'].mean().plot.bar(color=['green', 'gray'], ax=ax, title='The Average Monthly CPU Utilization Comparison')