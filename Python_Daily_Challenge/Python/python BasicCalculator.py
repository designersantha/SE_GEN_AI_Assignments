#!/usr/bin/env python3
"""
BasicCalculator.py
Day 2/50 – AI Python Challenge
A simple two‑number calculator supporting +, -, *, / operations.
"""

def calculate(a: float, b: float, op: str) -> float:
    """Return the result of applying `op` to `a` and `b`."""
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    raise ValueError(f"Unsupported operation: {op}")

def main() -> None:
    try:
        # 1️⃣  Collect numbers
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))

        # 2️⃣  Choose an operator
        operator = input("Choose an operation (+  -  *  /): ").strip()

        # 3️⃣  Compute and show the result
        result = calculate(x, y, operator)
        print(f"\n👉  {x} {operator} {y} = {result}\n")

    except ValueError as ve:
        print(f"❗ Input error: {ve}")
    except ZeroDivisionError as zde:
        print(f"❗ Math error: {zde}")

if __name__ == "__main__":
    main()
