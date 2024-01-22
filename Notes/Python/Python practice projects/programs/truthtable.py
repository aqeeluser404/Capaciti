def truth_table(x, y):
    # Define the NOT gate function
    def not_gate(value):
        return not value

    # Apply OR operator and NOT gate
    z = x or y
    result = not_gate(z)

    return result

# Get user input for x and y
x = int(input("Enter x as 1 or 0: "))
y = int(input("Enter y as 1 or 0: "))

# Calculate the result
output = truth_table(x, y)

# Print the result
print(f"The result (z) is: {output}")