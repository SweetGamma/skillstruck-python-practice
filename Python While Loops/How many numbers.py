total = 0  # Initialize a counter for the total numbers
number = int(input("Enter an integer (0 to stop): "))  # First input from the user

while number != 0:  # Keep running until the user enters 0
    total += 1  # Increment the counter
    number = int(input("Enter an integer (0 to stop): "))  # Ask for the next input

print(total)  # Print the total count of numbers
