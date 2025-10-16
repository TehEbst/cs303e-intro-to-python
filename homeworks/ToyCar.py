# File: ToyCar.py
# Student: Alex Medina
# UT EID: bam5767
# Course Name: CS303E
#
# Date: 2025-10-14
# Description of Program: This is a simple introductory assignment into classes. This file contains the ToyCar class
#   which provides the code for a car that can travel only in any 1 of the 4 major cardinal directions. Includes a
#   function that allows the user to specify coordinates for the car to travel to.

# Assignment Link
#   https://www.cs.utexas.edu/~byoung/cs303e/hw7.html

# Constants
#   The direction corresponds to angle of rotation counter-clockwise from the x-axis
EAST, NORTH, WEST, SOUTH = 0, 90, 180, 270

class ToyCar:

    def __init__(self, x = 0, y = 0, d = EAST):
        """The initializer for the class. By default, the coordinates of the car are
        (0,0) and the direction is EAST, which is also 0. For this program, we assume
        x and y are always integers, but we must validate that d is legal"""
        self.x = x
        self.y = y
        if self.validDir(d):
            self.d = d

    def __str__(self):
        """This function provides a string representation of the current car information"""
        return f"Your car is at location ({self.x}, {self.y}), heading {self.dirToCard()}"

    def validDir(self, d):
        """The purpose of this function is to check if the inputted direction is an integer
        ,and it is a cardinal direction only as defined in the constants section"""

        # Check that value is an integer
        if not isinstance(d, int):
            print( "ERROR: Illegal direction entered." )
            return False

        # Check that value is a valid cardinal direction
        if d != EAST and \
            d != NORTH and \
            d != WEST and \
            d != SOUTH:
            print( "ERROR: Illegal direction entered." )
            return False

        return True

    def setDir(self, n):
        # Validate inputted parameter is legal
        if self.validDir(n):
            # Update the current direction
            self.d = n
            print(f"DEBUG: setting direction {self.dirToCard()}")

    def getDir(self):
        return self.d

    def dirToCard(self):
        if self.d == EAST:
            return "East"
        elif self.d == NORTH:
            return "North"
        elif self.d == WEST:
            return "West"
        elif self.d == SOUTH:
            return "South"

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def turnLeft(self):
        """Change direction 90 degrees to the left"""
        if self.d != SOUTH:
            self.d += 90
        else:
            self.d = EAST

    def turnRight(self):
        """Change direction 90 degrees to the right"""
        if self.d != EAST:
            self.d -= 90
        else:
            self.d = 270

    def validMove(self, n):
        """Ensure move is an integer and non-negative"""
        if not isinstance(n, int):
            print( "ERROR: Illegal distance entered." )
            return False

        if n < 0:
            print( "ERROR: Illegal distance entered." )
            return False

        return True

    def forward(self, n):
        """Move the car in the current direction"""
        if self.validMove(n):
            if self.d == EAST:
                self.x += n
            elif self.d == NORTH:
                self.y += n
            elif self.d == WEST:
                self.x -= n
            elif self.d == SOUTH:
                self.y -= n
            print(f"DEBUG: moving forward {n}")

def goto( car, x, y):
    """Drive the car to the specified x, y coordinate. The car is of the class ToyCar"""
    # Figure out where car currently is
    currX = car.getX()
    currY = car.getY()

    # Move along x-axis accordingly
    nx = x - currX
    if nx != 0:
        # Determine our direction of movement
        if nx > 0:
            # Head east
            car.setDir(EAST)
        elif nx < 0:
            # Head west
            car.setDir(WEST)
        # Move correct amount of spaces
        car.forward(abs(nx))

    # Move along y-axis accordingly
    ny = y - currY
    if ny != 0:
        # Determine our direction of movement
        if ny > 0:
            # Head north
            car.setDir(NORTH)
        elif ny < 0:
            # Head south
            car.setDir(SOUTH)
        # Move correct amount of spaces
        car.forward(abs(ny))

def main():
    c1 = ToyCar(100, -100, SOUTH)  # Create car c1
    print(c1)  # and show its state

    c2 = ToyCar()  # create car c2
    print(c2)  # and show its state

    c3 = ToyCar(y=-50, d=90)  # create car c3
    print(c3)

    c = ToyCar(d=NORTH)  # create car c
    print(c)

    print(c.getDir())  # where is c headed?

    c.setDir(45)  # this should fail
    print(c)

    c.forward(100)  # move c forward 100
    print(c)

    c.turnLeft()  # turn c left
    print(c)

    c.forward(-50)  # this should fail

    c.forward(50)  # move c forward 50
    print(c)

    c.setDir(SOUTH)  # turn c toward the south
    print(c)

    c.turnRight()  # turn c right (West)
    print(c)

    c.forward(25)  # move c forward 25
    print(c)

    goto(c, 0, 0)  # call your external function
    print(c)  # to go to (0, 0)

    goto(c, 100, 100)  # now goto (100, 100)
    print(c)

    print(c.getX())  # get the current X
    print(c.getY())  # get the current Y

# main()