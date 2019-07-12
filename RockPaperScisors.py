
from random import choice

rock = "rock"
paper = "paper"
scisors = "scisors"

player1 = choice([rock, paper, scisors])
player2 = choice([rock, paper, scisors])

print(player1)
print(player2)

if player1 == player2:
    print("draw")
elif player1 == rock and player2 == scisors:
    print("player1")
elif player1 == paper and player2 == rock:
    print("player1")
elif player1 == scisors and player2 == paper:
    print("player1")
else:
    print("player2")
