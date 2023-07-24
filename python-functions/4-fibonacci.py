# Write a Python function called fibonacci_sequence that takes a number n as input and returns a list of the first n Fibonacci numbers.

def fibonacci_sequence(n):
    FIBONACCI_LIST = []
    n1, n2 = 0, 1

    for _ in range(n):
        FIBONACCI_LIST.append(n1)

        n1, n2 = n2, n1 + n2

    return FIBONACCI_LIST



print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))