start = input("Would you like to launch the game? enter yes or no: ")

def start_game():
    if start.lower() == "yes":  
        print("Initialization Complete")
    else:
        print("Initialization Failed")

start_game()  
