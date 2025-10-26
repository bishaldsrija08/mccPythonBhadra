
def add_student(name):
    with open("students.txt", "a") as file:
        file.write(name + "\n")
    
def view_students():
    with open("students.txt", "r") as file:
        data = file.read()
        print(data)
    
while True:
    choice = input("1. Add student\n2. View students\n3. Exit\nChoose an option: ")
    # \n New line for better readability
    if choice == '1':
        name = input("Enter student name: ")
        add_student(name) # Function call to add student
    elif choice == '2':
        view_students() # Function call to view students
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")