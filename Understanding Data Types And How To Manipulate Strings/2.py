# Instruction
# Write a program that adds the digits in a 2 ddigit number. e.g. if the input was 35, then the output shoulde be 3 + 5 = 8

# Warning.Do not change the code.Your program should work for different inputs. e.g. any two-digits number.Warning

two_digit_number = input("type a two digit number")
type(two_digit_number)

# print(type(two_digit_number))

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

print("First digit is :",first_digit)
print("Second digit is :",second_digit)

result =int( first_digit  )+ int(second_digit)
print("The additon of first digit", first_digit, "and second", second_digit," digit is", result)