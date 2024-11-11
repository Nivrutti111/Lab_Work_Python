# Input: number of terms
n = int(input("Enter the number of terms: "))

# Initialize the first two Fibonacci numbers
a, b = 0, 1
count = 0

print("Fibonacci series:")
# Use a while loop to generate Fibonacci series
while count < n:
    print(a, end=" ")  # Print the current Fibonacci number
    a, b = b, a + b   # Update a and b to the next Fibonacci numbers
    count += 1        # Increment the count

print()  # Print a newline at the end
