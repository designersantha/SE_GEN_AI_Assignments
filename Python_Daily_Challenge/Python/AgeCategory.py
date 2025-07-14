#!/usr/bin/env python3
"""
AgeCategory.py
Day 4/50 – AI Python Challenge
Determines whether a person is a Child, Teenager, Adult, or Senior based on age.
"""

def age_category(age: int) -> str:
    """
    Return the age category for the given age.
    - Child:     0–12
    - Teenager: 13–19
    - Adult:    20–59
    - Senior:   60+
    """
    if age < 0:
        return "Invalid age"
    if age <= 12:
        return "Child"
    if age <= 19:
        return "Teenager"
    if age <= 59:
        return "Adult"
    return "Senior"

def main() -> None:
    try:
        # Single age check
        age_input = input("Enter an age to categorize: ")
        age = int(age_input)
        print(f"Age {age} ➜ {age_category(age)}")
    except ValueError:
        print("❗ Please enter a valid integer for age.")

    # Optional list of ages
    try:
        ages_line = input("\nEnter multiple ages separated by spaces (or press Enter to skip): ").strip()
        if ages_line:
            ages = [int(a) for a in ages_line.split()]
            print("\nResults for the list:")
            for a in ages:
                print(f"Age {a} ➜ {age_category(a)}")
    except ValueError:
        print("❗ Please enter valid integers only.")

if __name__ == "__main__":
    main()
