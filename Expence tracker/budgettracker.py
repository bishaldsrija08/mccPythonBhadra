# Personal Budget Calculator using file handling (CLI application)

# function to save budget details to a file


def save_budget(income, expenses):
    with open("budget.txt", "w") as file:
        file.write(f"Income: {income}\n")  # \n means “go to the next line”.
        for item, amount in expenses.items():
            file.write(f"{item}:{amount}\n")  # For example: Food: 500, Travel: 200.
            total_expenses = sum(expenses.values())
            balance = income - total_expenses
            file.write(f"Total Expenses: {total_expenses}\n")
            file.write(f"Balance: {balance}\n")


# function to read budget details from a file
def read_budget():
    print("Budget Details:")
    try:
        with open("budget.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("No budget file found. Please save your budget first.")


def main():
    print("welcome to the Budget Tracker")
    print("1. Create and Save Budget")
    print("2. View Budget")
    choice = input("Enter your choice(1 or 2):")
    if choice == "1":
        income = float(input("Enter your total income:"))
        expenses = {}
        while True:
            item = input("Enter expense item (or type 'done' to finish):")
            if item.lower() == "done":
                break
            amount = float(input(f"Enter amount for {item}:"))
            expenses[item] = amount
            # food: 500, travel: 200
            save_budget(income, expenses)
            print("Budget saved successfully.")
    elif choice == "2":
        read_budget()
    else:
        print("Invalid choice. Please select 1 or 2.")


main()
