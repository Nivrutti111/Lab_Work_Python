#Q.2)WAP to get factorial of a number

# Get user input
n = int(input("Enter a number: "))

# Initialize factorial as 1 (since factorial of 0 is 1)
facto = 1

# Calculate factorial using for loop
for i in range(1, n + 1):
    facto *= i  # Multiply the current value of factorial by i

# Print the result
print(f"The facto of {n} is {facto}")
