number = 134572658345
def get_sum_of_digits_str(number: int):
    num_as_str = str(number)
    sum = 0
    for n in num_as_str:
        sum = sum + int(n)
    return sum

def get_sum_of_digits(number: int):
    sum = 0
    while number > 0:
        next_digit = number % 10
        sum = sum + next_digit
        number = number // 10
        print(number)

    return sum

print(get_sum_of_digits(number))

#print(number // 10)