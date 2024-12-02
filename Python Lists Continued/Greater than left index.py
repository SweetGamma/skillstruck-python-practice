my_list = [int(n) for n in input().split()]

current = my_list[0]

for x in my_list[1:]:
    if x > current:
        print(x, end=" ")
    current = x
