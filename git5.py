def fibonacci_series(n):
    if n <= 0:
        return "Please enter a positive integer"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        while len(fib_series) < n:
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

n = int(input("Enter the number of terms in the Fibonacci series: "))


fib_sequence = fibonacci_series(n)
print(f"The Fibonacci series up to {n} terms is: {fib_sequence}")