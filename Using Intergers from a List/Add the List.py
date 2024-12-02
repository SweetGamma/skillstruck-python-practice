my_list = [int(n) for n in input("Input a list of numbers").split()]


sum = 0
for x in my_list:
    sum += x
print(sum)