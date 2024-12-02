amanda_value = int(input("How many in Amanda's group?"))
jane_value = int(input("How many in Jane's group?"))

group = {
    "Fred" : 12,
    "Jackson" : 15,
    "Sophie" : 20,
    "Amanda" : amanda_value,
    "Jane" : jane_value,
}

total = 0

for people in group.values():
    total += people

print(total)
