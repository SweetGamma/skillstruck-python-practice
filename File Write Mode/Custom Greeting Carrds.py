answer = input("What would you like to say in your greeting card? ")


file = open("report.txt", "w")


file.write(answer)


file.close()


file = open("report.txt", "r")


print(file.read())


file.close()
