my_number = int(input("Pick a number: "))  # Initial input from the user
total = my_number  # Initialize total with the first input

while my_number != 0:  # Loop until the user enters 0
    my_number = int(input("Pick another number: "))  # Ask for the next input
    total += my_number  # Add the input to the total

print(total)  # Print the total sum
