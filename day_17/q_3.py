# WAP to find simple interest using function
# Formula to calculate `si = (ptr)/100

def calculate_simple_interest(principal, rate, time): # defining function
    si = (principal * rate * time) / 100
    return si # returning value

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))

simple_interest = calculate_simple_interest(p, r, t) # calling function
print(f"The simple interest is: {simple_interest}")