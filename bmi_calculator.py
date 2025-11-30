def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): "))

bmi = calculate_bmi(weight, height)
print("Your BMI is:", round(bmi, 1))

if bmi < 18.5:
    print("Category: Undrweight")
elif bmi < 25:
    print("Category: Normal") 
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")