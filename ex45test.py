# this is a test version that shows values. Final game will display only on command.

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
    
def hold_colors(color_list):
     hold_colors.color_list = color_list
     print "These are the color_list values: ", hold_colors.color_list
     return hold_colors.color_list
 
def choose_room(room_choice, hold_colors(hold_colors.color_list):
    r1_red, r1_blue, r1_orange,r2_red, r2_blue, r2_orange, r3_red, r3_blue, r3_orange = hold_colors(hold_colors.color_list)
     # distribute is recalculating the numbers.
      
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
    else:
        color = raw_input("Do you want red, blue or orange balls ? ")  
   

# implamenting the code
  
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

# could be in a player class

room_choice = raw_input("Do you want room1, room2, or room3? ")
choose_room(room_choice, hold_colors(hold_colors.color_list))
