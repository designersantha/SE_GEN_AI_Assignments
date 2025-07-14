#!/usr/bin/env python3
"""
PersonalGreeting.py
Day 1/50 – AI Python Challenge
Asks the user for their name, age, and favorite color, then prints
a personalized hello message.
"""

def main() -> None:
    # 1️⃣ Collect user input
    name = input("👋 What's your name? ")
    age = input("🎂 How old are you? ")
    color = input("🎨 What's your favorite color? ")

    # 2️⃣ Build a personalized message
    message = (
        f"\nHi {name}! At {age} years young, your love for {color} "
        f"shows you have a vibrant personality.\n"
        "Wishing you a colorful day ahead! 😊"
    )

    # 3️⃣ Display it
    print(message)


if __name__ == "__main__":
    main()
