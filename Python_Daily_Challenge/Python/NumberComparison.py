#!/usr/bin/env python3
"""
NumberComparison.py
Day 6/50 – AI Python Challenge
Compares two numbers and reports which is larger, smaller, or if they're equal.
"""

def main() -> None:
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if a > b:
            print(f"{a} is larger than {b}")
        elif a < b:
            print(f"{a} is smaller than {b}")
        else:
            print(f"{a} and {b} are equal")
    except ValueError:
        print("❗ Please enter valid numbers.")

if __name__ == "__main__":
    main()
