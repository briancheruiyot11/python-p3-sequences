#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return

# Start the sequence
    fib_sequence = [0, 1]

# Generate Fibonacci numbers
    while len(fib_sequence) < length:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)

# Print each number on its own line
    print(fib_sequence)
