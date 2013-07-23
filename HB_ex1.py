print "_" * 40

import random 

# getting name of player:
print "Hello there! What is your name? \nType name here:" ,
name = raw_input() 
print " "
 
 # the random generator--imported the random module:
comp_num = random.randint(1, 100)
print comp_num # this is for debugging

# greeting the player and introducing the game:
print "Welcome %s, I'm thinking of a number between 1 and 100.\nSee if you can guess the number in fewer than five guesses. \nYou can type your guess right here:"  % name ,
guess = int(raw_input())

# counting the guesses: 
count = 1
while guess != comp_num:
    count = count + 1 
    #comparing guess and comp_num
    if guess < comp_num:
        print "Your guess is too low, try again."
    else: 
        print "Your guess is too high, try again." 
            
    print "New guess? " ,
    new_guess = int(raw_input())
    guess = new_guess
                           
    if count < 5 and guess == comp_num:
       print "Yahoo, you guessed the number in", count, "tries."
    elif count >= 5:
       print "So sorry, you ran out of guesses."
       break

# skipping 
if (count == 1 and guess == comp_num):            
    print "Wow, first guess!"       
  
