import random

# Generate number between 1 and 100
secret_number = random.randint(1, 100)
guess = None
attempt = 0
while guess != secret_number:
    guess = int(input("Guess the number between 1 and 100: "))
    attempt = attempt + 1 # Increment attempt count
    # Comparing and feedback
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
        # Winning condition
    else:
        print("Congratulations! You've guessed the number!")
print(f"You found the number in {attempt} attempts.")