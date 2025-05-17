#Create an empty list to store numbers that meet the given condition.
numbers = []

# Iterate through numbers from 1000 to 3000 (inclusive)
for x in range(1000, 3000):
    # Check if the number is divisible by 7 but not by 5
    if (x % 7 == 0) and (x % 5 != 0):
        # If the conditions are met, append the number to the list
        numbers.append(x)

# Print the list of numbers as a comma-separated string
print(', '.join(map(str, numbers)))
