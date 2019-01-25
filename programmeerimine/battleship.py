from random import randint
#make gamefield
def updateGamefield():
    hit = "X"
    miss = "O"
    empty = "~"
    
#make ships class
class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
   
#get players guess and check it's inside the game area
x = 10
while x > 9:
    x = int(input("insert shots x coordinates: "))
    if x > 9:
        print("outside the playing field")
        
y = 10
while y > 9:
    y = int(input("insert shots y coordinates: "))
    if x > 9:
        print("outside the playing field")
        
#make a rndom ship
s1 = Ship(randint(0, 9), randint(0, 9))

#check if the shot hit
if s1.x == x and s1.y == y:
    print("It's a hit")
else:
    print("miss")
