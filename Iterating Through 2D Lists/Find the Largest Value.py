x = int(input("What is the first number?"))
y = int(input("What is the second number?"))
z = int(input("What is the third number?"))


my_list = [[0, 1, x], [10, 15, y], [100, 200, 300], [5, 6, z]]


largest = my_list[0][0]  


for i in range(4):  
    for j in range(3):  
        
        if my_list[i][j] > largest:
            largest = my_list[i][j]


print(largest)
