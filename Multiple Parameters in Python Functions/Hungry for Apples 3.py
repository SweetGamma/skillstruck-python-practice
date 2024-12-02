# Ask for three different fruits from the user
fruit1 = input("Please enter the name of the fruit you would like: ")
fruit2 = input("Please enter the name of the fruit you would like: ")
fruit3 = input("Please enter the name of the fruit you would like: ")

# Define the function with three parameters
def hungryForApples(fruit1, fruit2, fruit3):
    print(fruit1 + fruit2 + fruit3)  # Print them concatenated together

# Call the function, passing the three inputs
hungryForApples(fruit1, fruit2, fruit3)
