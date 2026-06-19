import random

print("===== Welcome to Prasham's Rock Paper Scissors Game =====")

choices = ["rock", "paper", "scissors"]

user_choice = input("Enter rock, paper, or scissors: ").lower()

computer_choice = random.choice(choices)

print("\nYou chose:", user_choice)
print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a Tie!")

elif (
    (user_choice == "rock" and computer_choice == "scissors") or
    (user_choice == "paper" and computer_choice == "rock") or
    (user_choice == "scissors" and computer_choice == "paper")
):
    print("You Win!")

elif user_choice in choices:
    print("Computer Wins!")

else:
    print("Invalid Input!")