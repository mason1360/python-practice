import random
c = random.choice(["rock", "paper", "scissors"])
u = input("rock/paper/scissors: ")
print("Draw" if u == c else "You lose" if (u,c) in [("rock","paper"),("paper","scissors"),("scissors","rock")] else "You win")
