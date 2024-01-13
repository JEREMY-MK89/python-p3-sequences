#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(length):
        fib_sequence.append(a)
        a, b = b, a + b
    print(fib_sequence)

# Test the function with length = 9
print_fibonacci(9)




