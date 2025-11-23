# Personal Budget Calculator using file handling (CLI application)

# function to save budget details to a file

def save_budget(income, expenses):
    with open("budget.txt", "w") as file:
        file.write(f"Income: {income}\n") # \n means “go to the next line”.
        for item, amount in expenses.item():
            file.write(f"{item}:{amount}\n") # For example: Food: 500, Travel: 200.
            total_expenses = sum(expenses.values())
            balance = income-total_expenses
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
    save_budget(5000, 2000)
    read_budget()
    
main()