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
    if n < 2:
        return 0

    ops, root = 0, 2

    while root <= n:
        # If n evenly divides by root
        if n % root == 0:
            # Total even-divisions by root = total operations
            ops += root
            # Set n to the remainder (integer division)
            n //= root
        else:
            # Increment root to find next potential factor
            root += 1

    return ops
