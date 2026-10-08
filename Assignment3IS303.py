import random

# Start the game
play_again = "y"

while play_again.lower() == "y":

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Keep track of valid guesses
    guess_count = 0

    print("\nI'm thinking of a number from 1 to 100.")

    while True:
        guess = int(input("Enter your guess: "))

        # Make sure the guess is between 1 and 100
        if guess < 1 or guess > 100:
            print("Invalid guess. Please enter a number between 1 and 100.")
            continue

        # Only valid guesses count
        guess_count += 1

        # Compare the guess to the secret number
        if guess < secret_number:
            print("Higher!")

        elif guess > secret_number:
            print("Lower!")

        else:
            print("Correct!")
            break

    # Print the player's results
    print(f"You got it in {guess_count} guesses!")

    if guess_count <= 3:
        print("Amazing!")
    elif guess_count <= 5:
        print("Impressive!")
    elif guess_count <= 7:
        print("Good job!")
    elif guess_count <= 9:
        print("Took a little longer, but you got there!")
    else:
        print("You need to lock in.")

    # Ask if the player wants to play again
    play_again = input("Would you like to play again? (Y/N): ")

print("Thanks for playing!")