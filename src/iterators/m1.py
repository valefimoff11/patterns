def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()

print(next(gen))
print(next(gen))

for a, i in enumerate(infinite_sequence()):
    print(i)
    if a >10:
        break