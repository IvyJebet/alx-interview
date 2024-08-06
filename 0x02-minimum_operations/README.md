# Minimum Operations Project

## Description
This project involves calculating the minimum number of operations needed to achieve exactly `n` characters `H` in a text file. The operations allowed are "Copy All" and "Paste". The goal is to find the most efficient sequence of these operations.

## Requirements
- Python 3.4.3
- Ubuntu 20.04 LTS

## Usage
To test the function, you can use the provided `0-main.py` script.

### Example
```python
#!/usr/bin/python3
"""
Main file for testing
"""

from 0-minoperations import minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
