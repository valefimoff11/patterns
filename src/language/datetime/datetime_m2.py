from dateutil import parser
#from datetime import datetime

#date/time specific regular expressions

# Test date strings
date_str1 = "2024-09-16"
date_str2 = "16th September, 2024"
date_str3 = "09/16/2024"

# Parsing date strings
date1 = parser.parse(date_str1)
date2 = parser.parse(date_str2)
date3 = parser.parse(date_str3)

print("Parsed Date 1:", date1)
print("Parsed Date 2:", date2)
print("Parsed Date 3:", date3)