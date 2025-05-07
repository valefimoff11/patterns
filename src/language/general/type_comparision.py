from decimal import Decimal

####################################
#
# object/type comparison
#
#####################################

p= 1.5
k = Decimal(1.5)

if type(p) is float:
    print("from type()")

if isinstance(p, float):
    print("from isinstance()")