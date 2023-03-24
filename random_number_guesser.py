import random
limit = int(input("Enter an upper limit for the range of numbers you will be guessing. It must be greater than 5"))
if limit <= 5:
    print("Enter a number greater than five")
guesses = 0

while True:
    guesses +=1
    r = random.randrange(1, limit+1)
    a = int(input("Enter your guess"))
    if a == r:
        print("You guessed correct")
        break;
    elif a<r:
        print("You guessed a lower number.")
    else:
        print("You guessed the correct number.")
    

print("It took",guesses,"guesses")
    
    
        
    
    
    