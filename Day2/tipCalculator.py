# Initial message
print("Welcome to Tip Calculator")
print("-------------------------------")

# Ask the user for the total bill amount
billInp = float(input("Your Total Bill : "))
tip = int(input("Percentage to be tipped (10/12/15) : "))
people = int(input("How many contributors : "))

# Calculating the tip amount
tipPercent = tip/100
billOp = billInp+(billInp*tipPercent)
perHead = billOp/people

# displaying answer
print("The contributuon per head is  : ",perHead)