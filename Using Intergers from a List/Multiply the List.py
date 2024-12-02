my_list = [int(n) for n in input("Choose 4 numbers to multiply with ").split()]

product = 1
for x in my_list:
    product = product *  x
print(product)

