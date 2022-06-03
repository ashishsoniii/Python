# Snake Water Gun game!
import random


def game(computer, player):

    if (computer == player):
        return None

    elif(computer == 's'):
        if player == 'w':
            return False
        elif player == 'g':
            return True
    elif(computer == 'w'):
        if player == 'g':
            return False
        elif player == 's':
            return True
    elif(computer == 'g'):
        if player == 's':
            return False
        elif player == 'w':
            return True


randno = random.randint(1, 3)
if(randno == 1):
    computer = 's'
elif((randno == 2)):
    computer = 'w'
elif(randno == 3):
    computer = 'g'

print("computer turn: Snake(s) water(w) or gun(g)? ")
player = int(input("Player's turn:  Snake(s) water(w) or gun(g)? "))
print(f"Computer choose {computer}")
print(f"You choose {player}")


a = game(computer, player)

if(a == True):
    print("YOU WIN!")
elif(a == None):
    print("Game is TIE!")
else:
    print("YOU LOOSE!")
