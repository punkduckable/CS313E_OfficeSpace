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



# Case class
class Case(object):
    # Constructor (+ helper methods)
    # This takes in height and width of the office, as well as a "cubicle
    # requests" dictionary. This dictionary houses requested cubicle of each
    # employee. The employees name is the key and their requested cubicle is
    # the value. h and w should be INTEGERS
    def __init__(self, h, w, cubicle_requests):
        self.h = h;
        self.w = w;
        self.cubicle_requests = cubicle_requests;

        self.office_area = h*w;
        self.allocated_area = self._calculate_allocated_area();
        self.unallocated_area = self.office_area - self.allocated_area;
        self.contested_area = self._calculate_contested_area();

    def _calculate_allocated_area(self):
        """Since the coordinate of every rectangle is an integer (as well as the
        diemsion of the office) we can find this area by "sweeping" through the
        x values in the office. For each x value, we sweep through the y values.
        for each y value, we check if the points (x,y) and (x+1,y+1) are
        in at least one of the rectangles. If they are, then the rectangle defined
        by (x,y) and (x+1,y+1) is covered, so we add one to the area. (otherwise
        the area remains unchanged). Doing this for all x,y gives us the total
        covered area. """
        area = 0;
        Rectangles = self.cubicle_requests.values();

        for x in range(self.w):
            for y in range(self.h):
                # Cycle through the rectangles. For each one, check if both
                # (x,y) and (x+1,y+1) is in that rectangle. If it is, then
                # we can increment the area by 1 and move on to the next y
                # value.
                for rec in Rectangles:
                    if (((x,y) in rec) and ((x+1, y+1) in rec)):
                        area +=1;
                        break;

        return area;


    def _calculate_contested_area(self):
        """ This function calculates the contested area in the office. The
        contested area is simply the sum of the area of the requested
        cubicles minus the total covered area.

        This method must be called AFTER the covered area has been calculate"""

        total_cubicle_area = 0;
        for rec in self.cubicle_requests.values():
            total_cubicle_area += rec.area();

        return total_cubicle_area - self.allocated_area;

    ############################################################################
    # Special methods
    def __str__(self):
        str  = "Total %d\n" % self.office_area;
        str += "Unallocated %d\n" % self.unallocated_area;
        str += "Contested %d\n" % self.contested_area;

        for (name, rec) in self.cubicle_requests.items():
            str += name + str(rec) + '\n';

        return str;
