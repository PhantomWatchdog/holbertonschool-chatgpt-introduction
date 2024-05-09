#!/usr/bin/python3
import sys

def factorial(n):
    """
    This function calculates the factorial of a given number using recursion.
    
    Parameters:
    n (int): The number for which the factorial is to be calculated.
    
    Returns:
    int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
f = factorial(int(sys.argv[1]))

print(f)
