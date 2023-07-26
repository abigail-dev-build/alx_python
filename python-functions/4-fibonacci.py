def fibonacci_sequence(n):
    FIBONACCI_LIST = []
    n1, n2 = 0, 1

    for _ in range(n):
        FIBONACCI_LIST.append(n1)

        n1, n2 = n2, n1 + n2

    return FIBONACCI_LIST
