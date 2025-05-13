from dateutil import parser
#from datetime import datetime

#Date/Time Validation Rule Types
#1. Date/Time Validation and Parsing through Explicitly/upfront specified, Date/time specific regular expressions
#2. Fully Automated date/time valdation and parsing - no upfront reg expression spec

###############################################################
# 2. Fully Automated date/time validation and parsing - no upfront reg expression spec required - however contains risks of semantically incorrect
# date misinterpretation, even though syntatcically correct
###############################################################

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