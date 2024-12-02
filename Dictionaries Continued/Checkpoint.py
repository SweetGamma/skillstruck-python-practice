coins = {
    "pennies": 1,
    "nickels": 5,
    "dimes": 10,
    "quarters": 25,
}

coins["silver dollar"] = 100

coins.pop("pennies")

print(coins)

print(len(coins))
