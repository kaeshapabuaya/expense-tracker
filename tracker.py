# project + installment tracker.py 
# Author: KAESHA C. PABUAYA
# Laboratory Activity 4 in Advanced Programming

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

if amt1 > 200:
    print(" Huge expense - are you sure?")
elif amt1 > 100:
    print(" Big expense.")
elif amt1 > 50:
    print(" Moderate expense.")
else:
    print(" Small expense.")
    
item2 = input("Second expense? ")
amt2 = float(input("Amount? "))

if amt2 > 200:
    print(" Huge expense - are you sure?")
elif amt2 > 100:
    print(" Big expense.")
elif amt2 > 50:
    print(" Moderate expense.")
else:
    print(" Small expense.")
    
taxper = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print("")

total = amt1 + amt2
ave = total / 2
tax = total * taxper / 100
gtotal = total + tax
obudget = gtotal > budget
budgetrem = budget - gtotal

print("-" * 40)
print("SUMMARY")
print(" - " + item1 + ": \t\t$" , amt1)
print(" - " + item2 + ": \t\t$" , amt2)
print("Total Spent: \t\t$" , total)
print("Average:      \t\t$" , ave)
print("Tax (" , taxper , ")     \t$" , tax)
print("Grand total:      \t$" , gtotal)

if obudget:
    print("Over budget by      \t$" , budgetrem , "!")
elif gtotal > budget * 0.90:
    print("Careful: only      \t$" , budgetrem , "left")
else:
    print("Within budget.      \t$" , budgetrem , "left")
print("-" * 40)

print("Made by: Kaesha C. Pabuaya | Installment 4\n")