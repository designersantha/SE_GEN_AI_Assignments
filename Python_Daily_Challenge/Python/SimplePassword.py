#!/usr/bin/env python3
"""
SimplePassword.py
Day 7/50 – AI Python Challenge
Checks if a password meets a minimum length requirement.
"""

MIN_LENGTH = 8

def main() -> None:
    password = input("Enter a password: ")

    if len(password) >= MIN_LENGTH:
        print("✅ Password accepted.")
    else:
        print(f"❌ Password too short. Must be at least {MIN_LENGTH} characters long.")

if __name__ == "__main__":
    main()
