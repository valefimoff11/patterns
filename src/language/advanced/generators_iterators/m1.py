import sys

#data pipelines / chains of generators possible too

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

print(infinite_sequence())
print(infinite_sequence())

sys.exit()

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

#resets the generator (current element pointer - to the start)
gen = infinite_sequence()

for a, i in enumerate(gen):
    print(f"{a}, {i}")
    if a > 10:
        break
