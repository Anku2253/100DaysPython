# ASCII Art for Treasure Island - Adds visual appeal at the start of the game
print('''
         *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')

# Welcome Message
print("Welcome to Treasure Island")
print("Your mission is to find the hidden treasure.")

# Game Starts - User is prompted to make the first choice at the crossroad
choice = input("You are at a crossroad. Do you want to go left or right? : ").lower()

# First Decision Point - Crossroad
if choice == "left":
    # If the player chooses left, they face a lake
    chc2 = input("You've come to a lake. You need to reach the island. Do you want to wait or swim? : ").lower()

    # Second Decision Point - Lake
    if chc2 == "wait":
        # If the player waits, a boat arrives, and they reach the island
        print("You've waited for a while and a boat has arrived. You've reached the island.")
        
        # On the island, the player must choose between three gates
        chc3 = input("You came across three gates. Which one would you open (Red, Yellow, Blue)? : ").lower()

        # Third Decision Point - Gate Selection
        if chc3 == "red":
            print("You got burned by fire. Game over")  # Red Gate - Fire trap
        elif chc3 == "yellow":
            print("You found the treasure.")  # Yellow Gate - Treasure found (Victory)
        else:
            print("You got eaten by beasts. Game over.")  # Blue Gate - Beast attack

    else:
        print("Game Over.")  # Swimming results in failure

else:
    print("Game Over")  # Choosing right at the crossroad leads to failure
