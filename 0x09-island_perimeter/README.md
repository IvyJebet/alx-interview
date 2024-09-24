## 0x09. Island Perimeter

## Description
This project involves creating a Python function to calculate the perimeter of an island in a grid. The grid is represented as a 2D list of integers, where:

- 0 represents water
- 1 represents land
The goal is to calculate the perimeter of the landmass (island) by analyzing the grid and determining the edges that contribute to the total perimeter.

## Learning Objectives
The project reinforces the following concepts:

- 2D Arrays (Matrices): Accessing, iterating over elements, and navigating adjacent cells.
- Conditional Logic: Applying conditions to check if a cell contributes to the perimeter.
- Counting Techniques: Developing a method to count the edges that form the perimeter.
- Python Programming: Using nested loops, conditionals, and Python's built-in data structures.

## Project Specifications
## Function: def island_perimeter(grid):
## Input: grid (A list of lists of integers)
- 0: Represents water
- 1: Represents land
## Output: Returns the perimeter of the island described in the grid
## Constraints:
- Each cell is square, with side length 1
- Cells are connected horizontally/vertically (not diagonally)
- The grid is rectangular with width and height not exceeding 100
- The grid is fully surrounded by water
- The island does not contain any lakes (i.e., no enclosed water)
