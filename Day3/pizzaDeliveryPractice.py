# Welcome Message
print("Welcome to Python Pizza Delivery")

# Initializing Bill
bill = 0  # The bill starts at $0 and increases based on user choices.

# Choosing Pizza Size
size = input("What size pizza do you want? S, M or L : ").upper()  # User inputs size, converted to uppercase to avoid case sensitivity issues.

# Size-Based Pricing
if size == "S":
    bill += 15  # Small pizza costs $15
elif size == "M":
    bill += 20  # Medium pizza costs $20
else:
    bill += 25  # Large pizza costs $25 (Default if not S or M)

# Choosing Pepperoni
pepperoni = input("Pepperoni for pizza (Y/N) : ").upper()  # User selects whether to add pepperoni
if pepperoni == "Y":
    if size == "S":
        bill += 2  # Small pizza with pepperoni costs $2 extra
    else:
        bill += 3  # Medium and large pizzas with pepperoni cost $3 extra

# Choosing Extra Cheese
cheese = input("Add extra cheese? (Y/N) : ").upper()  # User decides on extra cheese
if cheese == "Y":
    bill += 1  # Extra cheese adds $1 to the bill

# Displaying Total Bill
print(f"Your Total Bill is  : ${bill}")  # Final bill is displayed with f-string for easy formatting.
