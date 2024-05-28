def calculate_sum():
    total_sum = 0
    for number in range(1, 101):
        total_sum += number
    return total_sum


sum_result = calculate_sum()
print(f"The sum of all the numbers from 1 to 100 is: {sum_result}")


