'''
WAP  that asks for the user's age and check if they are eligible to participate in a competition.

Steps: 
1. Ask for the user's age using input().
2. Use if, elif and else to check conditions:
    - If age is below 10, print "Too young to participate."
    - If age is between 10 and 18, print"Eligible for the junior competiton"
    - If age is above 18, print "Eligible for the senior competition."
    '''

age = int(input("Enter your age: "))

if age<10: # age = 15 , 100<10
    print("Too young to participate.")
elif 10<=age<=18: # age range = 10 to 18, 100
    print("Eligible for junior competiton.")
else:
    print("Eligible for senior competition.") 