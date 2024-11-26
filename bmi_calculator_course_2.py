# Section Project: Calculate Body Mass Index
# ==========================================

# Print 'welcome' msg to the terminal
print("\n\nWELCOME TO THE BMI CALCULATOR")
print("=================================\n")

# Get the height from the user in 'cm'
height = int(input("Enter your height (cm): "))

# Convert the height from 'cm' to meters
height /= 100

# Get the weight from the user in 'lbs'
weight = int(input("Enter your weight (lbs): "))

# Convert the weight into 'kg'
weight /= 2.20462

# Calculate the BMI by squaring the height and dividing it by the weight
bmi = weight / (height * height)

bmi = round(bmi, 2)

# Print 'result' msg to the terminal
print("\n\nResult:\n=================================")
if bmi < 18.5:
  print("You are underweight!")
elif bmi < 30 and bmi >= 25:
  print("You are overweight!")
elif bmi >= 30:
  print("You are obese!")
else: 
  print("You are a healthy weight!")
print("Your BMI is: " + str(bmi))
