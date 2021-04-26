import random
number = random.randint(1,9)

chances = 0



while (chances < 5):
    
    guess = int(input("Guess a number between 1 through 9"))
    if (guess == number):
        chances = 6
    elif(guess > number):
            print("Your guess was too high")
            chances = chances+1
    elif(guess < number):
        print("Your guess was too low")
        chances = chances+1
    
if(chances == 5):
    print("No more chances, you lost")
    print("The correct number is ", number)
if(chances == 6):
    print("Congradulations, you won!")
    


