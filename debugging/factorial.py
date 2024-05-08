#!/usr/bin/python3
import sys

if len(sys.argv) < 2:
    print("Por favor, proporcione un número como argumento.")
    sys.exit(1)

def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n = n - 1
    return result

f = factorial(int(sys.argv[1]))
print(f)
