rows = input("Input a list of weather: ").split()


cols = ["windy", "breezy", "calm"]


list = [[(i + " " + j) for j in cols] for i in rows]


print(list)
