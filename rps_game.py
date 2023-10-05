import random
import sys

print("ROCK, PAPER,SCISSORS!")

#keep track of the wins,losses and ties

wins = 0
losses = 0
ties = 0

while True:
    print ("wins:"+ str(wins)+" losses:" + str(losses) + " ties:" + str(ties)+". Wanna play?")
#PlayerMove

    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == "q":
            print("Ty for coming!")
            sys.exit()
        elif playerMove == "r":
            print("ROCK!")
        elif playerMove == "p":
            print("PAPER!")
        elif playerMove == "s":
            print("SCISSORS")
        break
    #Computermove
    computerMove = random.randint(1,3)
    if computerMove == 1:
        print("against ROCK!")
    elif computerMove == 2:
        print("against PAPER!")
    elif computerMove == 3:
        print ("against SCISSORS!")


    #Win or Lose

    if playerMove == "r" and computerMove == 1 or playerMove == "p" and computerMove == 2 or playerMove == "s" and computerMove == 3:
        print("No one has won!")
        ties += 1
    elif playerMove == "r" and computerMove == 2 or playerMove == "p" and computerMove == 3 or playerMove == "s" and computerMove == 1:
        print ("Computer Won!")
        losses += 1
    elif playerMove == "r" and computerMove == 3 or playerMove == "p" and computerMove == 1 or playerMove == "s" and computerMove == 2:
        print ("You won!")
        wins += 1







