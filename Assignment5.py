# Sebastian Tapia assignment 5 
import random


# welcome player to game
print("Welcome to Rock Paper Scissors")
# ask how many round they would like to play
rounds = int(input("How many rounds would you like to play?: "))

while rounds % 2 == 0 or rounds <= 0:
    rounds = int(input("sorry enter a positive odd number: "))

# Function to get the player's choice
def get_player_choice():
    choice = input("Enter rock, paper, scissors: ").lower()

    while choice not in ["rock", "paper", "scissors"]:
        print("Sorry, that is not a valid choice. Please try again.")
        choice = input("Enter rock, paper, scissors: ").lower()

    return choice


# Function to determine who wins
def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif player == "rock" and computer == "scissors":
        return "win"
    elif player == "paper" and computer == "rock":
        return "win"
    elif player == "scissors" and computer == "paper":
        return "win"
    else:
        return "loss"


# variables to track wins and losses
player_wins = 0
computer_wins = 0

# keep playing until all rounds are completed
while player_wins + computer_wins < rounds:

    # Get choices
    player_choice = get_player_choice()
    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("The computer chose", computer_choice)

    # Determine the winner
    result = determine_winner(player_choice, computer_choice)

    if result == "tie":
        print("Tie! Play again.")

    elif result == "win":
        print("You won!")
        player_wins += 1

    else:
        print("You lost!")
        computer_wins += 1


# Display the final score
print("-------------------------------------------")
print("Score - You:", player_wins, "| Computer:", computer_wins)

if player_wins > computer_wins:
    print("You win!!!")
else:
    print("Computer wins!")

print("Thanks for playing!")