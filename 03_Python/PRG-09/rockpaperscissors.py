# functions
#function one checks move validity
#function two creates computer move
#function three checks score
#function four tracks score
#play for set number of rounds
import random
print("Let's play a game!")
print("Rules: rock beats scissors, scissors beats paper, paper beats rock")
print("You can only play [r]ock, [p]aper or [s]cissors")

def player_move():
    print("Round " + str(round+1))
    while True:
        move=input("3...2...1...shoot!")
        if move == ("r"):
            print("You played rock!")
            return 1
        elif move == ("p"):
            print("You played paper!")
            return 2
        elif move == ("s"):
            print("You played scissors")
            return 3
        
        else:
            print("Invalid option, try again")
            return player_move()

def computer_move():
    cmove= random.randint(1,3)
    if cmove == 1:
        print("Computer used rock!")
        return 1
    elif cmove == 2:
        print("Computer used paper!")
        return 2
    elif cmove == 3:
        print("Computer used scissors!")
        return 3

def compare_moves(move, cmove):
    if(move==1 and cmove==1) or (move==2 and cmove==2) or (move==3 and cmove==3):
        print("It's a tie!")
        return 0
    elif (move==1 and cmove==3) or (move==2 and cmove==1) or (move==3 and cmove==2):
        print("You win")
        return 1
    elif (move==1 and cmove==2) or (move==2 and cmove==3) or (move==3 and cmove==1):
        print("You lose")
        return -1

player_score=0
computer_score=0
round=0 