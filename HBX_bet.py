print "-" * 40
import random

#the random generator--imported from the module:
comp_num = random.randint(1,5)
print comp_num #used for debugging

# getting player's name
name = raw_input("Hi, what is your name? ")
print """
Welcome to my casino,%s. \nHow would you like to double your money quickly? \nAll you have to do is guess the correct number from 1 to 5, and bingo,\nyou have a stack of cash!
"""% name

bet = float(raw_input("How much is your bet? "))
guess = int(raw_input("What is your guess? "))
 
win = 0.10

count = 0
while win > 0.00:
    count += 1
    if comp_num != guess:
        win = (bet * 0.0)
        print "Too bad, you lose!"
    else:
        win = (bet * 2.0)
        print ("You won $%.2f!" % win)
        answer = raw_input("This time the range is 1 to 10. Do you want to try\nto double your money again? ")
        if answer == "no":
            print "Good-bye %s, check our gift shop on the way out!" % name
            break
        else:
            comp_num = random.randint(1,10)
            print comp_num #used for debugging
            
            bet = win
            new_guess = int(raw_input("New guess? "))
            guess = new_guess
                
                
 
