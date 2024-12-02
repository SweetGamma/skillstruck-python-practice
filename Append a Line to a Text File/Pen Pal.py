file = open("letter.txt", "a")


file.write("From your Pen Pal")


file.close()


file = open("letter.txt", "r")
print(file.read())


file.close()
