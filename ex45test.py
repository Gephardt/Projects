from random import randint

class Room(object):
    
    def __init__(self, red_ball, blue_ball, orange_ball):
        self.red_ball = red_ball                    
        self.blue_ball = blue_ball               
        self.orange_ball = orange_ball
              
        
class Bucket(object):
    
    def __init__(self,red_ball, blue_ball, orange_ball):
        self.red_ball_count = 0
        self.blue_ball_count = 0
        self.orange_ball_count = 0
       
        
         
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
              
red_ball = distribute()
blue_ball = red_ball
orange_ball = blue_ball
    
room1 = Room(red_ball, blue_ball, orange_ball)
room2 = Room(red_ball, blue_ball, orange_ball)
room3 = Room(red_ball, blue_ball, orange_ball)
