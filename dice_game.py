import random

dice = random.randint(1, 6)
    
print("🎲 Dice rolled")
print("Result:",dice)

if dice == 6:
    print("🔥 Jackpot!")
elif dice == 1:
    print("😅 Try again")
else:
    print("😉 Not bad")
