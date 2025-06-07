# Project 1: Create Snake, Water And gun game with python
# A simple game where user plays against computer in a rock-paper-scissors style game
# Snake beats Water, Water beats Gun, Gun beats Snake

import random

# Display game title
head = "Snake Water Gun Game."
print(head.title())

# Get number of rounds from user
n = int(input("Enter the no of Rounds: "))

# Define available game options and their relationships
option = ["s", "w", "g"]
winning_combinations = {
    "s": "w",  # Snake beats Water
    "w": "g",  # Water beats Gun
    "g": "s"   # Gun beats Snake
}

# Initialize game variables
round = 1
computer_win = 0
user_win = 0

# Main game loop
while round <= n:
    # Display round information and available moves
    print(f"Round {round} starts now \n Snake - s \n Water - w \n Gun -g ")
    
    # Get and validate user's choice
    users_choice = input("Enter your move: ")
    if users_choice not in option:
        print("Error You Entered an \"Invalid Move\" Try Again!")
        continue
    
    # Computer makes random choice
    computer_choice = random.choice(option)
    print(f"Computer chooses {computer_choice}")
    
    # Determine winner using the winning combinations
    if users_choice == computer_choice:
        print("Draw")
    elif winning_combinations[users_choice] == computer_choice:
        print("User win")
        user_win += 1
    else:
        print("Computer win")
        computer_win += 1

    round += 1

# Display final game results
if user_win > computer_win:
    print(f"You Won {user_win} Rounds")
    print(f"Congratulations You Won the Game!")
elif computer_win > user_win:
    print(f"Computer Won {computer_win} Rounds")
    print(f"Hardluck! You Lose.")
else:
    print(f"Both won {user_win} Rounds")
    print("Match is Draw!")
