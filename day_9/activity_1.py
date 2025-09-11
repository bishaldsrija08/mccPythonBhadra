'''
Activity:
Distribute pre-prepared buggy Python programs to students.
Ask students to identify errors using error messages and fix them.
Examples of bugs:
Missing parentheses in a print() statement.
Using incorrect variable names.
Logical errors in calculations.
Objective: Ensure every student can identify and fix at least one syntax and one logical error'''

# Buggy Python Program Example
def calculate_area(radius):
    # Intentional bug: missing parentheses in print statement
    print ("Calculating area...")
    
    # Intentional bug: incorrect variable name
    area = 3.14 * radius * radius  # 'radious' should be 'radius'
    
    return area
result = calculate_area(5)
print("Area:", result)