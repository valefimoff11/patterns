import sys

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

print(infinite_sequence())
print(infinite_sequence())


gen = infinite_sequence()


print(next(gen))
print(next(gen))

#gen.close()

for a, i in enumerate(infinite_sequence()):
    print(f"{a}, {i}")
    if a > 10:
        break

for a, i in enumerate(gen):
    print(f"{a}, {i}")
    if a > 10:
        break

gen = infinite_sequence()

for a, i in enumerate(gen):
    print(f"{a}, {i}")
    if a > 10:
        break
