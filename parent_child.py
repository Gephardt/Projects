class Parent(object):
    def rule(self):
        print "Clean your room."
        
    def rule2(self):
        print "Yes, I can."
        
    def girl(self):
        print "Get back here, young lady!"
        
    def boy(self):
        print "Get back here, buster!"
        
class Child(Parent):
    def rule(self):
        print "You can't make me!"
        
    def rule2(self):
        print "No, you can't."
        
    def rule3(self):
        print "Bite me. I never get to do anything fun!"
    
mom = Parent()
child = Child()
kid = 'boy'


mom.rule()
child.rule()
mom.rule2()
child.rule2()

if kid == 'girl':
    mom.girl()
else:
    mom.boy()
    
child.rule3()
