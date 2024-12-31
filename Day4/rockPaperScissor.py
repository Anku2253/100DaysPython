import random

# ASCII Art for Rock, Paper, and Scissors
ROCK = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Function to determine the winner based on choices
def game_logic(user_choice, computer_choice):
    """
    Game logic to determine the winner.

    Parameters:
    user_choice (int): The user's choice (0 for Rock, 1 for Paper, 2 for Scissors)
    computer_choice (int): The computer's random choice (0 for Rock, 1 for Paper, 2 for Scissors)

    Returns:
    None: Prints the result directly.
    """
    if user_choice == computer_choice:
        print("It's a tie")
    elif user_choice == 0 and computer_choice == 1:
        print("Paper covers rock, Computer wins")
    elif user_choice == 0 and computer_choice == 2:
        print("Rock smashes scissors, You win")
    elif user_choice == 1 and computer_choice == 0:
        print("Rock covers paper, You win")
    elif user_choice == 1 and computer_choice == 2:
        print("Scissors cuts paper, Computer wins")
    elif user_choice == 2 and computer_choice == 0:
        print("Rock smashes scissors, Computer wins")
    elif user_choice == 2 and computer_choice == 1:
        print("Scissors cuts paper, You win")
    else:
        pass

# Welcome message
print("Welcome to Rock Paper Scissors Game")

# User choice input and display
chc = int(input("What do you choose? Type 0 for Rock, 1 for paper, 2 for scissor : "))
if chc == 0:
    print(ROCK)
elif chc == 1:
    print(PAPER)
elif chc == 2:
    print(SCISSORS)
else:
    print("Invalid choice")

# Computer randomly selects a choice
comp = random.randint(0, 2)
print("Computer Choice")
if comp == 0:
    print(ROCK)
    game_logic(chc, comp)
elif comp == 1:
    print(PAPER)
    game_logic(chc, comp)
else:
    print(SCISSORS)
    game_logic(chc, comp)
