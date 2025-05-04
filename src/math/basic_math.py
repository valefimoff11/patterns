#1. English math terms for all situations
#2. Coding any math expression/equation in python
#3. Feeding the above with data / data processing / preparation for the above

#mat models, building block hierarchy
#Math Operators (+, -, *, **, sqrt) -> Math Functions (exp, ln etc) -> Math Models

import sys
import math
import numpy as np

#######################################################

#Python Numeric Types



#######################################################

#accurate summation

data = [0.1]*10
print(sum(data))
print(np.sum(data))
print(math.fsum(data))

sys.exit()

#######################################################

## Positive exponential notation
large_number = 1e6  ## 1 million
print(large_number)  ## Output: 1000000.0

## Negative exponential notation
small_number = 1e-3  ## 0.001
print(small_number)  ## Output: 0.001

## Mixed exponential notation
mixed_number = 3.14e2
print(mixed_number)  ## Output: 314.0

## Precision considerations
print(0.1 ** 3)     ## Floating point precision
print(1e-3)         ## Scientific notation equivalent

#######################################################

#Raise to the Power of N / Exponent
#raise x (base) to the power of n (exponent)
#Exponentiation, (power) x to the power y

x = 2
n = 3

print(x**n)
#output: 8

print(math.pow(2, 3))      ## Precise power calculation

#######################################################

#Modulo
#10 % 4 gives 2 because 10 divided by 4 leaves a remainder of 2.

rem = 10 % 4
print(rem)

#the rules for calculating modulo for negative values are differnt
print( 15 % -7)
print(15/-7)

#######################################################

#Floor division - returns the whole part rather than the remainder, in this way complements modulo
print(10//6)

#######################################################

#absolute value / module of number
print(abs(-5))

#######################################################

#take the square root of number
from math import sqrt
print(sqrt(4))

#######################################################

#The exponential function returns E raised to the power of x (E**x) / exponential growth
#'E' is the base of the natural system of logarithms (approximately 2.718282)
print(math.exp(2))
print(math.exp(2))         ## e raised to the power

print(np.exp(2))

#######################################################

#Euler’s constant, base of natural logarithms, Napier’s constant.
print(np.e)

print(math.log(100, 10))

#the logarithm to the base e of a number x
#the natural logarithm can be denoted ln
#the common logarithm (logarithm with base 10, usually written as log
#The natural logarithm log is the inverse of the exponential function, so that log(exp(x)) = x.
#The natural logarithm is logarithm in base e.

import numpy as np
print([1, np.e, np.e**2, 10])
print(np.log([1, np.e, np.e**2, 10]))


print(np.log10([1e-15, 100, -3.0]))

#######################################################

#Pi
print(np.pi)

#######################################################

#trigonometry functions
