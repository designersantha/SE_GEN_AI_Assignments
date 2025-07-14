#!/usr/bin/env python3
"""
ShoppingBill.py
Day 5/50 – AI Python Challenge
Calculates total cost of 3 items and applies tax percentage.
"""

def main() -> None:
    try:
        prices = []
        for i in range(1, 4):
            price = float(input(f"Enter price for item {i}: "))
            prices.append(price)

        tax_pct = float(input("Enter tax percentage (e.g., 5 for 5%): "))

        subtotal = sum(prices)
        tax_amount = subtotal * tax_pct / 100
        total = subtotal + tax_amount

        print(f"\nSubtotal: Rs.{subtotal:.2f}")
        print(f"Tax @ {tax_pct}%: Rs.{tax_amount:.2f}")
        print(f"Total: Rs.{total:.2f}\n")
    except ValueError:
        print("❗ Please enter valid numeric values.")

if __name__ == "__main__":
    main()
