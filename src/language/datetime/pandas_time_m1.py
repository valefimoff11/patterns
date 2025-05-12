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