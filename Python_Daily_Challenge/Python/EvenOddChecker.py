#!/usr/bin/env python3
"""
EvenOddChecker.py
Day 3/50 – AI Python Challenge
Checks if a number is even or odd, then evaluates a list of numbers.
"""

def check_even_odd(num: int) -> str:
    return "Even" if num % 2 == 0 else "Odd"

def main() -> None:
    # Check a single number
    try:
        number = int(input("Enter a number to check if it's Even or Odd: "))
        print(f"{number} is {check_even_odd(number)}.")
    except ValueError:
        print("Please enter a valid integer.")

    # Check a list of numbers
    try:
        numbers_input = input("Enter multiple numbers separated by spaces: ")
        numbers = [int(n) for n in numbers_input.split()]
        print("\nResult for the list:")
        for n in numbers:
            print(f"{n} is {check_even_odd(n)}")
    except ValueError:
        print("Please enter valid integers only.")

if __name__ == "__main__":
    main()
