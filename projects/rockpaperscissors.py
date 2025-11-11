import random

print("Welcome to Rock, Paper, Scissors!")
while True:
    user_choice = input("Enter your choice (rock, paper, scissors: ").lower()
    # ROCK => rock, PAPER => paper, SCISSORS => scissors
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input(
            "Invalid choice. Please enter rock, paper, or scissors: "
        ).lower()
    choices = ["rock", "paper", "scissors"]
    # Randomly select computer's choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and (computer_choice == "paper"))
    ):
        print("You win!")
    else:
        print("Computer wins!")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye.")
        break