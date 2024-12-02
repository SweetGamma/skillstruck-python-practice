name = input("Which tree do you want to remove? ")

trees = {
    "aspen": 75,
    "pine": 82,
    "maple": 60,
    "oak": 65,
    "willow": 80,
    "cottonwood": 100,  
}

trees.pop(name, None)  

print(trees)
