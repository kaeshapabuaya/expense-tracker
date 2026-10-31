# project + installment tracker.py 
# Author: KAESHA C. PABUAYA
# Laboratory Activity 5 in Advanced Programming

print("=" * 40)
print("            EXPENSE TRACKER")
print("       Know where your money goes.")
print("=" * 40)

name = input("\nWhat's your name? ")
taxper = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print("Welcome, " + name + "!\n" )

count = 0
choice = ""

print("MAIN MENU")
print("  [1] Add an expense")
print("  [2] View all expenses       (coming soon)")
print("  [3] Show total spent")
print("  [4] Exit\n")

subtotal = 0

while choice != "4":

    choice = input("Choose 1-4: ")

    if choice == "1":
        amt = float(input("Amount? "))
        subtotal += amt
        count += 1

        if amt > 200:
            print(" Huge expense - are you sure?")
        elif amt > 100:
            print(" Big expense.")
        elif amt > 50:
            print(" Moderate expense.")
        else:
            print(" Small expense.")

    elif choice == "2":
        print("Comin soon: The tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * taxper / 100
        gtotal = subtotal + tax
        obudget = gtotal > budget
        budgetrem = budget - gtotal

        print("Expenses:     \t\t" , count)
        print("Subtotal:      \t\t$" , subtotal)
        print("Tax (" , taxper , ")     \t$" , tax)
        print("Grand total:      \t$" , gtotal)

        if obudget:
            print("Over budget by      \t$" , budgetrem , "!")
        elif gtotal > budget * 0.90:
            print("Careful: only      \t$" , budgetrem , "left")
        else:
            print("Within budget.      \t$" , budgetrem , "left")

    elif choice =="4":
        print("Goodbye, " + name + "!\n" )
        print("-" * 40)
        print("Made by: Kaesha C. Pabuaya | Installment 5")
        print("=" * 40 , "\n")

    else:
        print(" Please choose 1, 2, 3, or 4.")
