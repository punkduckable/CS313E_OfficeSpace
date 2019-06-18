"""File: OfficeSpace.py

   Description:

   Student Name: Robert Stephany

   Student UT EID: rrs2558

   Course Name: CS 313E

   Unique Number: 85575

   Date Created: 06/18/2019

   Date Last Modified: 06/18/2019 """


# Interval class (used to build rectangles)
class Interval(object):
    # Constructor
    def __init__(self, a, b):
        self.a = a;
        self.b = b;

    ############################################################################
    # Non-special methods
    def length(self):
        return self.b - self.a;

    ############################################################################
    # Special methods
    def __str__(self):
        return "[%f %f]" % (self.a, self.b);

    def __contains__(self, x):
        # Checks if x is in [a,b]
        return (self.a <= x) and (x <= self.b);


class Rectangle(object):
    # Constructor.
    # Note: Rectangles are defined by specfifying the coordinates of the
    # southwest (lower left) and north east (upper right) corners.
    def __init__(self, sw_x, sw_y, ne_x, ne_y):
        self.x_range = Interval(sw_x, ne_x);
        self.y_range = Interval(sw_y, ne_y);

    ############################################################################
    # Non-special methods
    def area(self):
        return (self.x_range.length())*(self.y_range.length());

    ############################################################################
    # Special methods
    def __str__(self):
        return str(self.x_range) + "x" + self.y_range;

    # Note: coord is assumed to be a 2 component tuple of the form (x,y)
    def __contains__(self, coords):
        x,y = coords;
        return (x in self.x_range) and (y in self.y_range);
