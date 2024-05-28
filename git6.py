def sum_of_multiples():
    total_sum = 0
    for number in range(1, 1001):
        if number % 3 == 0 or number % 5 == 0:
            total_sum += number
    return total_sum

result = sum_of_multiples()
print(f"The sum of all numbers between 1 and 1000 that are divisible by 3 or 5 is: {result}")
