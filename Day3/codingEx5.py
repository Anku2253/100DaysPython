# Bmi Calculator
height = 1.65
weight = 84

# BMI calculation
BMI = (weight / (height**2))

#Displaying Bmi
print(f"Your BMI is: {round(BMI,2)}")

# interpretation of bmi
if BMI < 18.5:
    print("Underweight")
elif BMI>=18.5 and BMI<=25:
    print("Healthy Weight")
else:
    print("Overweight")

