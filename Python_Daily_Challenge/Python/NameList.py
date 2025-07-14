#!/usr/bin/env python3
"""
NameList.py
Day 10/50 – AI Python Challenge
Stores 5 names in a list and prints each with its length.
"""

def main() -> None:
    names = []
    for i in range(1, 6):
        name = input(f"Enter name {i}: ").strip()
        names.append(name)

    print("\nName list with lengths:")
    for name in names:
        print(f"{name} ({len(name)} characters)")

if __name__ == "__main__":
    main()
