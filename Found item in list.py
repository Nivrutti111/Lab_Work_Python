#Q.3)WAP to traverse a list of item and find particular item is present in the list or not

# Define a list of items
items = [10, 20, 30, 40, 50]

# Get user input for the item to search
search = int(input("Enter the item to search: "))

# Flag variable to track if the item is found
found = False

# Traverse the list using a for loop
for item in items:
    if item == search:
        found = True
        break  # Exit the loop if item is found

# Check if the item was found and print the result
if found:
    print(f"The item {search} is present in the list.")
else:
    print(f"The item {search} is not present in the list.")
