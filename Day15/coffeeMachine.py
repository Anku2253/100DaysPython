# Coffee Menu Configuration
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 50,
            "coffee": 24
        },
        "cost": 3.0
    }
}

# Initial Resource Stock
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

# Initial Profit
profit = 0


# Function to Check Resource Availability
def isSufficient(res, chc):
    """Checks if there are enough resources to make the selected drink.

    Args:
        res (dict): Available resources.
        chc (str): Selected drink (espresso/latte/cappuccino).

    Returns:
        bool: True if resources are sufficient, False otherwise.
    """
    for item in res:
        if res[item] < menu[chc]["ingredients"][item]:
            return False  # Return False if any ingredient is insufficient
        return True  # Return True if all resources are available


# Function to Display Current Resource Report
def showReport(res):
    """Displays the current stock of resources and profit."""
    for keys in res:
        print(f"{keys} : {res[keys]}ml")  # Prints resource levels
    print(f"Money : ${profit:.2f}")  # Prints profit earned


# Function to Process Coins for Payment
def processCoins():
    """Calculates the total value of coins inserted by the user.

    Returns:
        float: Total calculated amount from coins.
    """
    print("Please insert coins.")
    total = int(input("How many quarters? : ")) * 0.25
    total += int(input("How many dimes? : ")) * 0.1
    total += int(input("How many nickles? : ")) * 0.05
    total += int(input("How many pennies? : ")) * 0.01
    return total


# Function to Dispense Coffee and Update Resources
def vendCoffee(chc, menu):
    """Processes payment, dispenses coffee, and updates resources.

    Args:
        chc (str): The selected drink.
        menu (dict): Menu containing ingredient requirements and cost.
    """
    payment = processCoins()

    if payment < menu[chc]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    elif payment >= menu[chc]["cost"]:
        print(f"Tu {chc} mi amor 🤎 ☕ 🧋 ")  # Coffee is successfully dispensed
        change = round(payment - menu[chc]["cost"], 2)
        print(f"Here is your change: ${change}")

        global profit
        profit += menu[chc]["cost"]  # Update profit with the cost of the coffee

        # Deduct used resources from the available stock
        resources["coffee"] -= menu[chc]["ingredients"]["coffee"]
        resources["water"] -= menu[chc]["ingredients"]["water"]
        resources["milk"] -= menu[chc]["ingredients"]["milk"]


# Function to Manage Coffee Making Process
def processCoffee(chc, res, menu):
    """Manages coffee preparation by checking resource availability.

    Args:
        chc (str): Selected drink (espresso/latte/cappuccino).
        res (dict): Available resources.
        menu (dict): Menu with ingredient requirements.
    """
    if isSufficient(resources, chc):
        vendCoffee(chc, menu)
    else:
        print("Sorry, insufficient resources to process your order.")


# Main Program Loop
isOn = True

while isOn:
    # Ask the user for their coffee choice
    choice = input("What would you like? (espresso/latte/cappuccino) : ")

    # Turn off the machine if 'off' is entered
    if choice == "off":
        isOn = False
    # Display the resource report if 'report' is entered
    elif choice == "report":
        showReport(resources)
    # Process coffee orders based on user selection
    elif choice == "espresso":
        processCoffee(choice, resources, menu)
    elif choice == "latte":
        processCoffee(choice, resources, menu)
    elif choice == "cappuccino":
        processCoffee(choice, resources, menu)
