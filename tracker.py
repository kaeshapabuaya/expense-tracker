# project + installment tracker.py 
# Author: KAESHA C. PABUAYA
# Laboratory Activity 2 in Advanced Programming
print("=" * 40)
print("            EXPENSE TRACKER")
print("       Know where your money goes.")
print("=" * 40)

print("\nMAIN MENU")
print("  [1] Add an expense           (coming soon)")
print("  [2] View all expenses        (coming soon)")
print("  [3] Show total spent         (coming soon)")
print("  [4] Exit                     (coming soon)\n")

name = input("What's your name? ")
print("Welcome, " + name + "! Let's log two expenses.\n" )

item1 = input("First expense? ")
amt1 = float(input("Amount? "))
item2 = input("Second expense? ")
amt2 = float(input("Amount? "))
print("")

total = amt1 + amt2
ave = total / 2

print("-" * 40)
print("SUMMARY")
print(" - " + item1 + ": \t$" , amt1)
print(" - " + item2 + ": \t$" , amt2)
print("Total Spent: \t$" , total)
print("Average:      \t$" , ave)

print("-" * 40)
print("Made by: Kaesha C. Pabuaya | Installment 2\n")