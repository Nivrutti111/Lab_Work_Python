#1. Using input function take two number and then swap the number
# Take input from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Print original numbers
print("Before swapping:")
print("num1 =", num1)
print("num2 =", num2)

# Swap using third variable
temp = num1
num1 = num2
num2 = temp

# Print swapped numbers
print("After swapping:")
print("num1 =", num1)
print("num2 =", num2)



