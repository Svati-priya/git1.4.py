def sum_of_digits(number):
    total_sum = 0
    while number > 0:
        digit = number % 10
        total_sum += digit
        number //= 10
    return total_sum


num = int(input("Enter a number: "))


sum_digits = sum_of_digits(num)
print(f"The sum of all the digits of {num} is: {sum_digits}")