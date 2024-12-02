file = open("your_text_file.txt", "r")

data = file.read()


words = data.split()


print("Number of words:", len(words))

file.close()
