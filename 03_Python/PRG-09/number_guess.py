import random
count = 0
number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
 
while (number!= 'guess'):
    if guess < number:
        print("The number guessed is too low")
        count = count+1
        guess = int(input("Guess a number between 1 and 100: "))
    elif (guess > number):
        print("The number guessed is too high")
        count = count+1
        guess = int(input("Guess a number between 1 and 100: "))
    else:
        print("The number guessed is right")
        print("The number of tries is", count+1) 
        break