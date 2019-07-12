
from random import choice

rock = "rock"
paper = "paper"
scisors = "scisors"

player1 = choice([rock, paper, scisors])
player2 = choice([rock, paper, scisors])

print("Welocme in rock, paper, scisors game\n")
print("player 1 choose the "+ str.upper(player1))
print("player 2 choose the "+ str.upper(player2))

if player1 == player2:
    print("This is DRAW,try once again")
elif player1 == rock and player2 == scisors:
    print("player 1 win")
elif player1 == paper and player2 == rock:
    print("player 1 win")
elif player1 == scisors and player2 == paper:
    print("player 1 win")
else:
    print("player 2 win")

