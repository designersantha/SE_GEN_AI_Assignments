#!/usr/bin/env python3
"""
GradeAverage.py
Day 11/50 – AI Python Challenge
Calculates the average of 5 test scores and determines pass/fail.
"""

PASS_MARK = 50  # Adjust as needed

def main() -> None:
    try:
        scores = []
        for i in range(1, 6):
            score = float(input(f"Enter score {i}: "))
            if not 0 <= score <= 100:
                raise ValueError("Scores must be between 0 and 100.")
            scores.append(score)

        average = sum(scores) / len(scores)
        status = "PASS" if average >= PASS_MARK else "FAIL"

        print(f"\nAverage score: {average:.2f}")
        print(f"Result: {status}")
    except ValueError as ve:
        print(f"❗ {ve}")

if __name__ == "__main__":
    main()
