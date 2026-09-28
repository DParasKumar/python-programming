# Write a program that calculates the body maass index from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weight the same amount, the short person is usally more overwight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m).
# formula : BMI = weight(kg)/height^2

print("Welcome to BMI Calculator")
print("Please Enter your weight and height:")

height = int(input("Enter your height:"))
weight = int(input("Enter your weight:"))

result = weight / height ** 2
print("your BMI is:",result)

