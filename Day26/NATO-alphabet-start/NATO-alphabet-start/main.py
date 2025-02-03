import pandas as pd

# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
data = pd.read_csv(r"Day26\NATO-alphabet-start\NATO-alphabet-start\nato_phonetic_alphabet.csv")
dataDict = {row.letter:row.code for (index,row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word : ").upper()
l = [dataDict[letter] for letter in word]
print(l)

