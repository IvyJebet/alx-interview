## 0x08. Making Change

## Project Overview
This project tackles the classic Coin Change Problem, a well-known challenge in both dynamic programming and greedy algorithms. The objective is to determine the minimum number of coins needed to make up a given total, based on a list of coin denominations. The challenge lies in designing an efficient algorithm that can compute the solution in the least amount of time, while ensuring correctness.

## Key Concepts
## 1. Greedy Algorithms
- Greedy algorithms attempt to solve the problem by making the locally optimal choice at each step, hoping that these choices will lead to a globally optimal solution.
- However, there are scenarios where greedy algorithms fail to provide the correct result for certain coin denominations, so understanding its limitations is crucial.
## 2. Dynamic Programming
- Dynamic programming is a more robust approach when greedy algorithms do not work. It involves breaking the problem into smaller sub-problems, solving each sub-problem only once, and storing their results.
- Key principles include optimal substructure (a solution can be built from solutions to sub-problems) and overlapping sub-problems (solving the same sub-problem multiple times).
## 3. Algorithmic Complexity
- The efficiency of the solution will be measured by its time and space complexity.
- Strive for a solution that handles large inputs within acceptable runtime limits.
## 4. Python Programming
- This project requires solid knowledge of Python, including:
- List manipulation and comprehensions.
= Efficient use of loops and conditionals.
- Writing functions with minimal runtime overhead.

## Task Breakdown
## - Objective
 - Given a set of coin denominations, find the minimum number of coins needed to make a given total.
## - Prototype
 - def makeChange(coins, total):
## - Parameters
 - coins: A list of available coin denominations.
 - total: The amount for which you need to determine the minimum number of coins.
## - Return
 - The fewest number of coins needed to meet the total.
 - If the total is 0 or less, return 0.
 - If the total cannot be made with the given coins, return -1.

## Resources
- Greedy Algorithms
- Dynamic Programming - Coin Change Problem
- Python Official Documentation
