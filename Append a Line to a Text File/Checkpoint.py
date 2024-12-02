file = open("your_text_file.txt", "a")


file.write("I love programming!")


file.close()


file = open("your_text_file.txt", "r")


print(file.read())


file.close()
