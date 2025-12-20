import random
n = random.randint(1, 5)
g = int(input("Guess (1-5): "))
print("You win!" if g == n else f"You lose! It was {n}")
