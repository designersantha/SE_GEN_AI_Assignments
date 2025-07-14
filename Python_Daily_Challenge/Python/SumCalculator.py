#!/usr/bin/env python3
"""
SumCalculator.py
Day 9/50 – AI Python Challenge
Calculates the sum of all numbers from 1 to n using a loop.
"""

def main() -> None:
    try:
        n = int(input("Enter a positive integer n: "))
        if n < 1:
            raise ValueError("n must be positive.")

        total = 0
        for i in range(1, n + 1):
            total += i

        print(f"The sum of numbers from 1 to {n} is {total}")
    except ValueError as ve:
        print(f"❗ {ve}")

if __name__ == "__main__":
    main()
