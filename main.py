import json
import os
import datetime

DATA_FILE = "expenses.json"
VALID_CATEGORIES = [
    "Food", "Transport", "Housing", "Utilities",
    "Entertainment", "Health", "Shopping", "Other"
]


def get_valid_amount():
    """
    Ask the user for an expense amount and keep asking until they
    give a positive number. Rejects non-numeric input and amounts
    that are zero or negative.
    """
    while True:
        raw_amount = input("Enter amount: $").strip()
        try:
            amount = float(raw_amount)
            if amount <= 0:
                print("Amount must be greater than zero. Try again.")
                continue
            return round(amount, 2)
        except ValueError:
            print("Error: Invalid input")

def get_valid_date():
    # Asking for a date, or use today's date if the user just press Enter
    while True:
        date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
        if date_input == "":
            today = datetime.date.today()
            return str(today)
        try:
            valid_date = datetime.datetime.strptime(date_input, "%Y-%m-%d")
            return valid_date.strftime("%Y-%m-%d")
        except ValueError:
            print("Please enter the date like this: 2026-09-27")

def get_valid_category():
    categories = ["Food", "Transport", "Bills", "Fun", "Other"]

    print("\nChoose a category:")
    for i in range(len(categories)):
        print(str(i + 1) + ". " + categories[i])

    while True:
        choice = input("Enter category number: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a number.")
            continue

        if choice >= 1 and choice <= len(categories):
            return categories[choice - 1]

        print("Please select a number from 1 to " + str(len(categories)))


def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        file = open(DATA_FILE, "r")
        expenses = json.load(file)
        file.close()
        return expenses

    except:
        print("Unable to load saved expenses.")
        return []


def save_data(expenses):
    with open(DATA_FILE,"w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    print("\nAdd New Expense")

    amount = get_valid_amount()
    date = get_valid_date()
    category = get_valid_category()

    new_expense = {
        "amount": amount,
        "date": date,
        "category": category
    }

    expenses.append(new_expense)
    save_data(expenses)

    print("Expense added successfully.")


def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\nYour Expenses:")

    for i in range(len(expenses)):
        expense = expenses[i]

        print(
            str(i + 1) + ". " +
            expense["date"] + " | " +
            expense["category"] + " | $" +
            str(expense["amount"])
        )


def edit_expense(expenses):
    view_expenses(expenses)

    if len(expenses) == 0:
        return

    number = input("Enter the expense number you want to edit: ")

    try:
        number = int(number)
    except ValueError:
        print("Please enter a valid number.")
        return

    if number < 1 or number > len(expenses):
        print("Invalid expense number.")
        return

    position = number - 1

    print("\nEnter the new details:")

    expenses[position]["amount"] = get_valid_amount()
    expenses[position]["date"] = get_valid_date()
    expenses[position]["category"] = get_valid_category()

    save_data(expenses)

    print("Expense updated successfully.")


def delete_expense(expenses):
    view_expenses(expenses)

    if len(expenses) == 0:
        return

    number = input("Enter the expense number you want to delete: ")

    try:
        number = int(number)
    except ValueError:
        print("Please enter a valid number.")
        return

    if number < 1 or number > len(expenses):
        print("Invalid expense number.")
        return

    position = number - 1

    expenses.pop(position)
    save_data(expenses)

    print("Expense deleted successfully.")


def export_to_csv(expenses):
    if len(expenses) == 0:
        print("There are no expenses to export.")
        return

    file = open("expenses.csv", "w")

    file.write("Date,Category,Amount\n")

    for expense in expenses:
        file.write(
            expense["date"] + "," +
            expense["category"] + "," +
            str(expense["amount"]) + "\n"
        )

    file.close()

    print("Expenses saved to expenses.csv")


def category_summary(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return

    totals = {}
    total_money = 0

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        total_money = total_money + amount

        if category in totals:
            totals[category] = totals[category] + amount
        else:
            totals[category] = amount

    print("\nCategory Summary")

    for category in totals:
        amount = totals[category]
        percentage = (amount / total_money) * 100

        print(
            category + ": $" +
            str(round(amount, 2)) +
            " (" + str(round(percentage, 1)) + "%)"
        )


def check_budget(expenses):
    budget = input("Enter your monthly budget: $")

    try:
        budget = float(budget)
    except ValueError:
        print("Please enter a valid amount.")
        return

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("\nTotal spent: $" + str(round(total, 2)))

    if total > budget:
        extra = total - budget
        print(
            "You have gone over your budget by $" +
            str(round(extra, 2)))
    else:
        remaining = budget - total
        print(
            "You are within your budget. $" +
            str(round(remaining, 2)) +
            " is remaining.")

def display_menu():
    # Print a simple menu with ASCII borders
    print("========================================")
    print("           EXPENSE TRACKER")
    print("========================================")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Edit expense")
    print("4. Delete expense")
    print("5. Export to CSV")
    print("6. Category summary")
    print("7. Check budget")
    print("8. Exit")
    print("========================================")


def main():
    # Load any expenses that were saved from last time
    expenses = load_data()

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            edit_expense(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            export_to_csv(expenses)
        elif choice == "6":
            category_summary(expenses)
        elif choice == "7":
            check_budget(expenses)
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()