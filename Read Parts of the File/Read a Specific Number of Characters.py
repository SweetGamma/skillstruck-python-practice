number = int(input("How many characters do you want to print?"))


file = open("your_text_file.txt", "r")


print(file.read(number))


file.close()
