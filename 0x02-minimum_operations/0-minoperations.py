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
        # Check if the current divisor is a factor of n
        while n % divisor == 0:
            # Add the divisor to operations
            operations += divisor
            # Divide n by the divisor
            n //= divisor
        # Move to the next potential factor
        divisor += 1

    return operations
