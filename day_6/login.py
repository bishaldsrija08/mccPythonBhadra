
# Write a program that keeps asking the user for a password until they enter "Python123".

my_password = "Python123"
password=""
while password!=my_password:
    password = input("Enter your password: ")
print("You are logged in!")