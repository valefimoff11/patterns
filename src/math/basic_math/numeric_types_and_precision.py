from decimal import Decimal

import math

print(1.1 + 2.2)

p= 1.5
k = Decimal(1.5)

print(type(p))
print(type(k))
print(type(math.sqrt(k)))
print(type(k.sqrt()))

if type(p) is float:
    print("sucess")

if isinstance(p, int):
    print("jjj")