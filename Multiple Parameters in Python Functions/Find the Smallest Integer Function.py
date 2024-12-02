# Ask the user for two integers
choice1 = int(input("What is the first number?"))
choice2 = int(input("What is the second number?"))

# Define the function to find the smallest number
def my_function(first, second):
    if first < second:
        print(first)  # Print the first number if it is smaller
    else:
        print(second)  # Print the second number if it is smaller

# Call the function with the two inputs
my_function(choice1, choice2)
