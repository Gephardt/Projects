# BallGame: this game will allow the user 10 tries to fill the three colored buckets with the correct colored balls from each of the three rooms. The player goes to each room and asks for a particular color. If that color is in the room, the balls are added to the coresponding bucket total. Each bucket should have 10 balls before 10 tries or the player loses.

# This is a test version that shows values. Final game will display only on command.

# CURRENT PROBLEM: distribute function will recalculate balls when call in the choose_room function
# CURRENT PROBLEM: how to choose a different room while still in the while loop
# CURRENT PROBLEM: do not know how to work the interplay amoung functions. Don't know how to return needed variables to other functions

from random import randint
     
class Room(object):
     def __init__(self, red_ball, blue_ball, orange_ball):
        self.red_ball = red_ball                    
        self.blue_ball = blue_ball               
        self.orange_ball = orange_ball


class Bucket(object):
    
      def __init__(self,red_ball_count, blue_ball_count, orange_ball_count):
        self.red_ball_count = red_ball_count
        self.blue_ball_count = blue_ball_count
        self.orange_ball_count = orange_ball_count
                  
        print "~" * 30
        print "RED BUCKET HAS: %r" % self.red_ball_count    
        print "~" * 30
        print "BLUE BUCKET HAS: %r" % self.blue_ball_count
        print "~" * 30
        print "ORANGE BUCKET HAS: %r" % self.orange_ball_count
        print "~" * 30
        
def distribute():
    print
    r1_red = randint(0,10)
    r1_blue = randint(1,10)
    r1_orange = randint(0,10)
    print "ROOM ONE"
    print "red: %r" % r1_red
    print "blue: %r" % r1_blue
    print "orange: %r" % r1_orange
    print "-" * 20
             
    r2_red = randint(0,10 - r1_red)
    r2_blue = randint(0,10 - r1_blue)
    r2_orange = randint(0,10 - r1_orange)
    print "ROOM TWO"
    print "red: ", r2_red
    print "blue: ", r2_blue
    print "orange: ", r2_orange
    print "-" * 20
          
    r3_red = (10 - (r1_red + r2_red))
    r3_blue = (10 - (r1_blue + r2_blue))
    r3_orange = (10 - (r1_orange + r2_orange))
    print "ROOM THREE"
    print "red: ", r3_red
    print "blue: ",  r3_blue
    print "orange: ",  r3_orange
    print "-" * 20 
       
    color_list = [r1_red, r1_blue, r1_orange,r2_red, r2_blue, r2_orange, r3_red, r3_blue, r3_orange]
    return color_list
    
 
def choose_room(room_choice):
    r1_red, r1_blue, r1_orange,r2_red, r2_blue, r2_orange, r3_red, r3_blue, r3_orange = distribute()
     # distribute is recalculating the numbers.
    
    count = 0
    while count < 3: # this number is for testing, will increase in final game
         
        if room_choice == 'room1':
            color = raw_input("Do you want red, blue or orange balls ? ")
            if color == 'red':
               total_red_ball_count = red_ball_count + r1_red
               print total_red_ball_count
            elif color == 'blue':
                total_blue_ball_count = blue_ball_count + r1_blue
                print total_blue_ball_count
            else:
                total_orange_ball_count = orange_ball_count + r1_orange
                print total_orange_ball_count
            
        elif room_choice == 'room2':
            color = raw_input("Do you want red, blue or orange balls ? ")
            if color == 'red':
                total_red_ball_count = red_ball_count + r2_red
                print total_red_ball_count
            elif color == 'blue':
                total_blue_ball_count = blue_ball_count + r2_blue
                print total_blue_ball_count
            else:
                total_orange_ball_count = orange_ball_count + r2_orange
                print total_orange_ball_count
             
        else:
            color = raw_input("Do you want red, blue or orange balls ? ")
            if color == 'red':
                total_red_ball_count = red_ball_count + r3_red
                print total_red_ball_count
            elif color == 'blue':
                total_blue_ball_count = blue_ball_count + r3_blue
                print total_blue_ball_count
            else:
                total_orange_ball_count = orange_ball_count + r3_orange
                print total_orange_ball_count
                 
        count += 1 
        
   

# implementing the code
  
red_ball = distribute()
blue_ball = red_ball
orange_ball = blue_ball

red_ball_count = 0
blue_ball_count = 10
orange_ball_count = 0 
    
room1 = Room(red_ball, blue_ball, orange_ball)
room2 = Room(red_ball, blue_ball, orange_ball)
room3 = Room(red_ball, blue_ball, orange_ball)

three_buckets = Bucket(red_ball_count, blue_ball_count, orange_ball_count)


room_choice = raw_input("Do you want room1, room2, or room3? ")
choose_room(room_choice)
