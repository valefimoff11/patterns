import numpy as np
import pandas as pd
from dateutil import parser
from datetime import datetime

# Date/Time Validation Rule Types (all validation rule types are also implemented in pandas and numpy date/time handling functions)
# 1. Date/Time Validation and Parsing through Explicitly/upfront specified, Date/time specific regular expressions
# 2. Fully Automated date/time validation and parsing - no upfront reg expression spec

###############################################################
# 1. Date/Time Validation and Parsing through Explicitly/upfront specified, Date/time specific regular expressions
###############################################################

# input date
date_string = '2017-12-31'

# giving the date format
date_format = '%Y-%m-%d'

# using try-except blocks for handling the exceptions
try:

   # formatting the date using strptime() function
   dateObject = datetime.strptime(date_string, date_format)
   print(dateObject)

# If the date validation goes wrong
except ValueError:

   # printing the appropriate text if ValueError occurs
   print("Incorrect data format, should be YYYY-MM-DD")

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

    # Parsing and validating date strings with Pandas (based on dateutil internally)
    dti = pd.to_datetime(
        ["2018-1-22", np.datetime64("2018-01-01"), datetime(2018, 1, 1)]
    )


# If the date validation goes wrong
except ValueError:

   # printing the appropriate text if ValueError occurs
   print("Incorrect data format")

print("Parsed Date 1:", date1)
print("Parsed Date 2:", date2)
print("Parsed Date 3:", date3)

print(dti)