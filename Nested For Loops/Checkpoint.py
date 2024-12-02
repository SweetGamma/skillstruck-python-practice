rows = 3


pets = ["dog", "cat", "rabbit", "hamster", "parrot"]


list = [[pet for pet in pets] for i in range(rows)]

print(list)
