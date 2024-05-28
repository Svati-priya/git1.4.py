def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        while n > 1:
            result *= n
            n -= 1
        return result

number = int(input("Enter a number to find its factorial: "))


print(f"The factorial of {number} is {factorial(number)}")

