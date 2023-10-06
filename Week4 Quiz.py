
# Fibonacci Sequence
    fib_current = 1
    fib_prior = 0
    while fib_current < 10000:
        print(f'Fibonacci value is {fib_current}')
        fib_current, fib_prior = fib_current + fib_prior, fib_current
    print(f'First Fibonacci value greater than 10,000 is {fib_current}')