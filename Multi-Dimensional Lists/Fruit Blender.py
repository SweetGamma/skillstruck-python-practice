cols = ["apple", "grape", "peach", "cinnamon", "vanilla"]


rows = input("Input a list of fruits: ").split()


list = []


for i in rows:
    col = []
    
    for j in cols:
        
        col.append(i + " " + j)
    
    list.append(col)


print(list)
