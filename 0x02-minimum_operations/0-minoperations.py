#!/usr/bin/python3
"""
Module to calculate the minimum number of operations to achieve n characters
in a text file using only "Copy All" and "Paste" operations.
"""

def minOperations(n):
    """
    Returns the fewest number of operations needed to result in exactly n H characters.
    :param n: Target number of characters
    :return: Minimum number of operations or 0 if n is impossible to achieve
    """
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    return operations
