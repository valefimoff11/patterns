from decimal import Decimal

####################################
#
# object/type and value comparison and
# passing objects by ref and value
#
####################################

p= 1.5
k = Decimal(1.5)

# "is" - python identity operator
if type(p) is float:
    print("from type()")

if isinstance(p, float):
    print("from isinstance()")

a = [1, 2, 3]
b = [4, 5, 6]

def pass_param(a):

    a.append(10)
    return 10

pass_param(b)

print(b)

a = [1, 2, 3]
b = a.copy()

#compare the value
print(a==b)
#compare object addresses ie whether the vars point at the same object in terms of identical address in ram
print(a is b)

#this is based on the fact that there is a singleton list type (which in turn is an object)
#also type check / identification /test - 2 key approaches
print(type(a))
print(type(a) is list)
print(isinstance(a, list))

x = None
print(x == None)
#the preferd way for None comparison
print(x is None)
print(type(x))
print(type(None))

#get the ram address of object
print(id(None))


########################################################

