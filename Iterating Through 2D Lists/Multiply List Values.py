my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]
rows = 4
cols = 3

answer = int(input("What do you want to multiply by?"))


for i in range(rows):
    
    for j in range(cols):
        my_list[i][j] *= answer


print(my_list)
