"""Powerball Lottery Simulator
   A fun simulation of the lottery experience without spending money.
   Tags: short, humor, simulation
"""

import random
import sys  # For exit functionality

def get_player_numbers():
    """Prompt the player to enter 5 unique numbers between 1 and 69."""
    while True:
        print("Enter 5 different numbers from 1 to 69, separated by spaces (or type 'exit' to quit):")
        response = input("> ")
        if response.lower() == "exit":
            print("Thanks for playing! Goodbye!")
            sys.exit()

        # Validate the input length and uniqueness
        numbers = response.split()
        if len(numbers) != 5:
            print("Please enter exactly 5 numbers.")
        continue

        try:
            # Convert strings to integers
            numbers = [int(num) for num in numbers]
        except ValueError:
            print("Please enter valid numbers (e.g., 27, 35, or 62).")
            continue

        if any(num < 1 or num > 69 for num in numbers):
            print("All numbers must be between 1 and 69.")
            continue

        if len(set(numbers)) != 5:
            print("All numbers must be unique.")
            continue

        return numbers


def get_powerball_number():
    """Prompt the player to enter the Powerball number between 1 and 26."""
    while True:
        print("Enter the Powerball number (between 1 and 26, or type 'exit' to quit):")
        response = input("> ")
        if response.lower() == "exit":
            print("Thanks for playing! Goodbye!")
            sys.exit()

        try:
            powerball = int(response)
            if 1 <= powerball <= 26:
                return powerball
            print("The Powerball number must be between 1 and 26.")
        except ValueError:
            print("Please enter a valid number (e.g., 3, 15, or 22).")


def get_number_of_plays():
    """Prompt the player to enter how many times they want to play."""
    while True:
        print("How many times do you want to play? (Max: 1,000,000, or type 'exit' to quit):")
        response = input("> ")
        if response.lower() == "exit":
            print("Thanks for playing! Goodbye!")
            sys.exit()

        try:
            num_plays = int(response)
            if 1 <= num_plays <= 1_000_000:
                return num_plays
            print("You can play between 1 and 1,000,000 times.")
        except ValueError:
            print("Please enter a valid number (e.g., 3, 15, or 22000).")


def simulate_lottery(player_numbers, player_powerball, num_plays):
    """Simulate the Powerball lottery."""
    price = "$" + str(2 * num_plays)
    print(f"\nIt costs {price} to play {num_plays} times. Good luck!")
    input("Press Enter to start (or type 'exit' to quit at any time)...")

    possible_numbers = list(range(1, 70))
    for play in range(num_plays):
        # Generate random lottery numbers
        random.shuffle(possible_numbers)
        winning_numbers = sorted(possible_numbers[:5])  # Winning numbers in sorted order
        winning_powerball = random.randint(1, 26)

        # Display the winning numbers
        print(f"Winning numbers: {', '.join(map(str, winning_numbers))} and Powerball {winning_powerball}")

        # Check if the player has won
        if set(player_numbers) == set(winning_numbers) and player_powerball == winning_powerball:
            print("\nYou have won the Powerball Lottery! Congratulations!")
            print("You would be a billionaire if this was real!")
            return

    print("\nSorry, you lost.")
    print(f"You have wasted {price}. Thanks for playing!")


# Main execution starts here
print("""Powerball Lottery Simulator
A fun way to experience the thrill of playing the lottery without spending a dime!

Each ticket costs $2. The jackpot is $1.586 billion!
The odds of winning are 1 in 292,201,338. Good luck!
(Type 'exit' at any prompt to quit the game.)
""")

while True:
    # Get player input
    player_numbers = get_player_numbers()
    player_powerball = get_powerball_number()
    num_plays = get_number_of_plays()

    # Simulate the lottery
    simulate_lottery(player_numbers, player_powerball, num_plays)

    # Ask if the player wants to play again
    print("\nWould you like to play again? (yes or no)")
    play_again = input("> ").lower()
    if play_again not in ["yes", "y"]:
        print("Thanks for playing! Goodbye!")
        break
