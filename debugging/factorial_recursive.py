#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number recursively.

    Parameters:
    n (int): The number for which the factorial is to be calculated.

    Returns:
    int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the input number from command line argument
f = factorial(int(sys.argv[1]))
print(f)
