import random
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

wordList = ["aardvark","baboon","camel"]

lives = 6

choosenWord = random.choice(wordList)
print(choosenWord)

placeHolder = ""

for i in choosenWord:
    placeHolder+="_ "

print(placeHolder)

gameOver = False
correctLetter = []

while not gameOver:
    guess = input("Guess the letter from the word : ").lower()

    display = ""

    for i in choosenWord:
        if i==guess:
            display += i + " "
            correctLetter+=guess
        elif i in correctLetter:
            display += i + " "
        else:
            display += "_ "

    print(display)

    if guess not in choosenWord:
        lives -= 1
        if lives == 0:
            gameOver=True
            print("You Lose")

    if "_" not in display:
        gameOver = True
        print("Congratulations you won!")

    print(stages[lives-6])




