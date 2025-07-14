#!/usr/bin/env python3
"""
CountNumbers.py
Day 8/50 – AI Python Challenge
Counts positive, negative, and zero numbers in a list.
"""

def main() -> None:
    try:
        nums = [int(n) for n in input("Enter integers separated by spaces: ").split()]
        positives = sum(1 for n in nums if n > 0)
        negatives = sum(1 for n in nums if n < 0)
        zeros = sum(1 for n in nums if n == 0)

        print(f"Positives: {positives}")
        print(f"Negatives: {negatives}")
        print(f"Zeros: {zeros}")
    except ValueError:
        print("❗ Please enter integers only.")

if __name__ == "__main__":
    main()
