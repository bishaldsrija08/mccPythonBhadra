
task =[]  # Empty list to store tasks

while True:
    print("\n To-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Sort Tasks")
    print("5. Exit")
    choice = int(input("Enter your choice: ")) # Take user input and convert to integer

    if choice ==1: # Add Task
        task_name = input("Enter the task name: ")
        task.append(task_name)
    elif choice ==2: # View Tasks
        print("Your Tasks:")
        for i in range(len(task)):
            print(f"{i+1}. {task[i]}")
    elif choice ==3: # Remove Task
        task_index = int(input("Enter the task number to remove form 1: ")) - 1
        if 0<=task_index <len(task):
            task.pop(task_index)
            print("Task removed.")
    elif choice ==4: # Sort Tasks
        task.sort()
        print("Tasks sorted alphabetically.")
    elif choice ==5: # Exit
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please try again.")