import sys

import numpy as np
import pandas as pd
from dateutil import parser
from datetime import datetime

#key attributes for date/time parsing/validation rules and input data scenarios:
#date, timestamp (and its precision), time zone, locality (of the date-time)

# Date/Time Validation Rule Types (all validation rule types are also implemented in pandas and numpy date/time handling functions)
# 1. Date/Time Validation and Parsing through Explicitly/upfront specified, Date/time specific regular expressions
# 2. Fully Automated date/time validation and parsing - no upfront reg expression spec

###############################################################
# 1. Date/Time Validation and Parsing through Explicitly/upfront specified, Date/time specific regular expressions
###############################################################

# input date
date_string = '2017-12-31'

# date formats
date_format1 = '%Y-%m-%d'
date_format2 = '%Y-%m-%d-%H-%M-%S-%z'

try:

   # formatting the date using strptime() function
    date1_p = datetime.strptime(date_string, date_format1)
    date2_p = datetime.strptime('2018-04-18-17-04-30-+1000', date_format2)

    dateparser = lambda date_val: datetime.strptime(date_val, '%Y-%m-%d %H:%M:%S')
    #deprecated - use date_format
    df = pd.read_csv("E:\\pyprojects\\patterns\\patterns\\sampledata\\server_util.csv", parse_dates=['datetime'], date_parser=dateparser)
    df = pd.read_csv("E:\\pyprojects\\patterns\\patterns\\sampledata\\server_util.csv", parse_dates=['datetime'], date_format='%Y-%m-%d %H:%M:%S')

    #df['datetime'] = df['datetime'].apply(lambda x: x.strftime('%d%m%Y'))

    df1 = pd.DataFrame({'date': ['2022-05-01', '2022-05-02', '2022-05-03']})
    # convert to datetime using pd.to_datetime
    df1['date'] = pd.to_datetime(df1['date'])
    print(df1)

    df1 = pd.DataFrame({'date': ['2022-05-01', '2022-05-02', '2022-05-03']})
    df1['date'] = df1['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    print(df1)

    df = pd.DataFrame({'date': ['2022-05-01', '2022-05-02', '2022-05-xx']})
    print(df)
    #generates ValueError and converts to NaT
    #df['date'] = pd.to_datetime(df['date'])
    # convert to datetime using pd.to_datetime and handle missing datetime data
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    print(df)
    #df['date'] = df['date'].astype('datetime64[ns]')
    #df['date'] = pd.to_datetime(df['date'], format='%d%b%Y:%H:%M:%S.%f', errors='coerce')
    # for multiple columns
    #df[['start', 'end']] = df[['start', 'end']].apply(pd.to_datetime, format='%d%b%Y:%H:%M:%S.%f', errors='coerce')

    print(df.dtypes)
    df.info()


# If the date validation goes wrong
except ValueError:

   # printing the appropriate text if ValueError occurs
   print("Incorrect data format, should be YYYY-MM-DD")

print("Parsed Date_1_p:", date1_p)

print("TZ NAME: {tz}".format(tz=date2_p.tzname()))
print("Parsed Date_2_p:", date2_p)

print()

###############################################################
# 2. Fully Automated date/time validation and parsing - no upfront reg expression spec required - however contains risks of semantically incorrect
# date misinterpretation, even though syntatcically correct
###############################################################

# Test date strings
date_str1 = "2024-09-16"
date_str2 = "16th September, 2024"
date_str3 = "09/16/2024"

try:

    # Parsing and validating date strings
    date1 = parser.parse(date_str1)
    date2 = parser.parse(date_str2)
    date3 = parser.parse(date_str3)

    # Parsing and validating date strings with Pandas (which is still based on dateutil internally)
    date4 = pd.to_datetime(
        ["2018-1-22", np.datetime64("2018-01-01"), datetime(2018, 1, 1)]
    )

    df1 = pd.DataFrame({'date': ['2022-05-01', '2022-05-02', '2022-05-03']})
    #infer_datetime_format is deprecited - it is now the default
    df1['date'] = pd.to_datetime(df1['date'], infer_datetime_format=True)
    print(df1)


# If the date validation goes wrong
except ValueError:

   print("Incorrect data format")

print("Parsed Date 1:", date1)
print("Parsed Date 2:", date2)
print("Parsed Date 3:", date3)

print("Parsed Date 5:", date4)
