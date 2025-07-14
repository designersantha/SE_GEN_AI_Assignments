#!/usr/bin/env python3
"""
CountdownTimer.py
Day 12/50 – AI Python Challenge
Simple countdown from 10 to 0.
"""

import time

def main() -> None:
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)
    print("Blast off!")

if __name__ == "__main__":
    main()
