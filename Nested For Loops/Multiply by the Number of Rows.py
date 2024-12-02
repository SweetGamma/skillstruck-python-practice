rows = int(input("How many rows do you want?"))
mylist = [1, 2, 3, 4, 5]
list = [[(j * rows) for j in mylist] for i in range(rows)]

print(list)
