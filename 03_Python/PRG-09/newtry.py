# functions
#function one checks move validity
#function two creates computer move
#function three checks score
#function four tracks score
#play for set number of rounds
from ctypes import wintypes
import random

from 03_Python.PRG-09.rps import compare_moves

player_score=0
computer_score=0
round=0

def welcome_message():
    print("Let's play a game!")
    print("Rules: rock beats scissors, scissors beats paper, paper beats rock")
    print("When I say shoot, you pick [r]ock, [p]aper or [s]cissors")
    print("Here we go!")

round=0
def player_move():
    print("Round " + str(round))
    while True:
        move=input("3...2...1...shoot! ")
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
        print("Computer played rock!")
        return 1
    elif cmove == 2:
        print("Computer played paper!")
        return 2
    elif cmove == 3:
        print("Computer played scissors!")
        return 3

if (player_move==computer_move):
    print("It's a tie!")
elif (player_move==1 and computer_move==3) or (player_move==2 and computer_move==1) or (player_move==3 and computer_move==2):
    print("You win")
    player_score=player_score+1
    print(str("Player Score" + player_score))
    print(str("Computer Score" + computer_score))
elif (player_move==1 and computer_move==2) or (player_move==2 and computer_move==3) or (player_move==3 and computer_move==1):
    print("You lose")
    computer_score=computer_score+1
    print(str("Player Score" + player_score))
    print(str("Computer Score" + computer_score))



welcome_message()

player_move()
computer_move()

("Round " + str(round))
while round<10:
    round=round+1


print("--------------------------------------------------------------------------------------------")
print("Game Over")
print("Final Score:")
print("Player Score: " + str(player_score))
print("Computer Score: " + str(computer_score))
if player_score>computer_score:
    print("You Win!")
elif player_score<computer_score:
    print("You Lose...")
elif player_score==computer_score:
    print("It's a tie")



for round(0,10)

for( i in 1:10){
    gedoe computer_move
    gedoe player_move
    ronde score = wie wintypes
    lijst_player[[i]] = player score 
    lijst_computer[1] 
}


compare_moves(player())