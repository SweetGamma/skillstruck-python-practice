my_list = [int(n) for n in input().split()]
biggest = 0
for x in my_list:
    if x > biggest:
        biggest = x

print(biggest)
