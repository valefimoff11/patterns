# importing parser from dateutil module
from dateutil import parser

# input date
date_string = '23-41-2021'
date_string = '23-1-2021'

# printing the input date
print("Input Date:", date_string)

# using try-except blocks for handling the exceptions
try:

   # parsing the date string using parse() function
   # It returns true if the date is correctly formatted else it will go to except block
   print(bool(parser.parse(date_string)))

# If the date validation goes wrong
except ValueError:

   # printing the appropriate text if ValueError occurs
   print("Incorrect data format")


#########################################


# importing datetime module
import datetime

# input date
date_string = '2017-12-31'

# giving the date format
date_format = '%Y-%m-%d'

# using try-except blocks for handling the exceptions
try:

   # formatting the date using strptime() function
   dateObject = datetime.datetime.strptime(date_string, date_format)
   print(dateObject)

# If the date validation goes wrong
except ValueError:

   # printing the appropriate text if ValueError occurs
   print("Incorrect data format, should be YYYY-MM-DD")