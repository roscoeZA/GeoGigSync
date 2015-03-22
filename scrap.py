__author__ = 'roscoe'
class Classy():
    def __init__(self):
        print "init"
        self.x = 0
        self.variable = self.setter(self.x)

    def setter(self, x):
        if x == 0:
            return "x=0"
        elif x == 1:
            return "x = 1"

    def printer(self):
        print self.variable

x = Classy()
x.printer()

