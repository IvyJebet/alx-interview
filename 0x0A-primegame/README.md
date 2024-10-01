## 0x0A. Prime Game

## Project Overview
This project is part of the ALX Interview preparation and is designed to challenge your understanding of prime numbers, game theory, and algorithm optimization using Python. It revolves around a competitive game where players, Maria and Ben, strategically remove prime numbers and their multiples from a set of integers, with the objective of determining the winner based on optimal play.

The goal is to implement a function isWinner(x, nums) to determine the winner of multiple rounds of this game.

## Game Description
1. Players: Maria and Ben.

2. Objective: In each round, players alternately pick a prime number and remove it along with its multiples from a set of integers. The player unable to make a valid move loses the round.

3. Rounds: There are x rounds, where nums is an array containing the set size n for each round.

4. Assumptions:
 - Maria always plays first.
 - Both players play optimally.
 - n and x will not exceed 10,000.

## Key Concepts

## Prime Numbers
- A prime number is a natural number greater than 1 with no divisors other than 1 and itself.
- Efficiently identifying prime numbers in the range is key to solving the problem.
## Sieve of Eratosthenes
- An algorithm used to find all primes up to a given limit, which is particularly useful for this task.
## Game Theory
- Maria and Ben must make strategic choices based on available prime numbers, with optimal play ensuring the best chances of winning.
## Dynamic Programming
- Previous results can be cached to optimize performance when handling multiple rounds.
## Resources

## Prime Numbers:
- Introduction to Prime Numbers
- Sieve of Eratosthenes in Python

## Game Theory:
- Game Theory Basics

## Dynamic Programming:
- Dynamic Programming with Python Examples
