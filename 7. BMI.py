mass = float(input("Enter mass in KG: "))     # in kilograms
height = float(input("Enter height in Meters:"))   # in meters

bmi = mass / (height ** 2)

print(f"BMI: {bmi:.2f}")
