import random

# List of available characters for password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message to the user
print("Welcome to the PyPassword Generator!")

# User input for password configuration
nr_letters = int(input("How many letters would you like in your password? : ")) 
nr_symbols = int(input("How many symbols would you like? : "))
nr_numbers = int(input("How many numbers would you like? : "))

# Easy Level Password Generation (Ordered Password)
password = ""

# Generate random letters based on user input
for char in range(nr_letters):
    password += random.choice(letters)

# Generate random symbols based on user input
for i in range(nr_symbols):
    password += random.choice(symbols)

# Generate random numbers based on user input
for i in range(nr_numbers):
    password += random.choice(numbers)

# Display the generated password (easy level)
print(password)

# Hard Level Password Generation (Shuffled Password)
passList = []

# Append random letters to the list
for char in range(nr_letters):
    passList += random.choice(letters)

# Append random symbols to the list
for i in range(nr_symbols):
    passList += random.choice(symbols)

# Append random numbers to the list
for i in range(nr_numbers):
    passList += random.choice(numbers)

# Shuffle the list to randomize character order for increased security
random.shuffle(passList)

# Join the shuffled list into a single string
password = ''.join(passList)

# Display the final secure password (hard level)
print(password)
