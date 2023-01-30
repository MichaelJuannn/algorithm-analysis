import random
def coinToss():
    return random.choice(["Heads", "Tails"])
#3 kali melempar koin
result = [coinToss(),coinToss(),coinToss(),coinToss()]
headChance = result.count('Tails')
print("The chance resulting in Tails is :",headChance,"/ 4")