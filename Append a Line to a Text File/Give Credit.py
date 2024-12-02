file = open("report.txt", "a")


file.write("Quote was said by Gandhi")

file.close()

file = open("report.txt", "r")
print(file.read())


file.close()
