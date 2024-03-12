def fibonacci_sequence(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    return fib_sequence[:n]


n = 10
result = fibonacci_sequence(n)
print(f"The first {n} numbers of the Fibonacci sequence: {result}")
