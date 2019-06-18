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
        return str(self.x_range) + "x" + str(self.y_range);

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

        # Calculate the various areas.
        self.office_area = h*w;
        self.allocated_area = self._calculate_allocated_area();
        self.unallocated_area = self.office_area - self.allocated_area;
        self.contested_area = self._calculate_contested_area();

        # Now, calculate the guaranteed areas for each employee.
        self.guaranteed_area = {};
        for name in cubicle_requests:
             self.guaranteed_area[name] = self._calculate_guaranteed_area(name);


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
        """ This method calculates the contested area in the office. The
        contested area is simply the sum of the area of the requested
        cubicles minus the total covered area.

        This method must be called AFTER the covered area has been calculate"""

        total_cubicle_area = 0;
        for rec in self.cubicle_requests.values():
            total_cubicle_area += rec.area();

        return total_cubicle_area - self.allocated_area;


    def _calculate_guaranteed_area(self, name):
        """ This method calculates the guaranteed area for the employee named
        "name". To do this, I sweep through the x range of name's cubicle
        request. for each y value, I sweep through the y range. For each y
        value, I determine if the square defined by the points (x,y) and
        (x+1, y+1) has been claimed by another employee. If so, then the
        employees contested area is incremented by one.

        Once the contested area has been determined, we return the cubicle
        area minus the contested area. """

        contested_area = 0;
        cubicle = self.cubicle_requests[name];
        x_min = cubicle.x_range.a;
        x_max = cubicle.x_range.b;
        y_min = cubicle.y_range.a;
        y_max = cubicle.y_range.b;

        for x in range(x_min, x_max):
            for y in range(y_min, y_max):
                # cycle through the other employees
                for employee, rec in self.cubicle_requests.items():
                    # skip name (otheriwse everything would be contested)
                    if(employee == name):
                        continue;

                    if (((x,y) in rec) and ((x+1, y+1) in rec)):
                        contested_area +=1;
                        break;

        return cubicle.area() - contested_area;

    ############################################################################
    # Special methods
    def __str__(self):
        # Print office parameters
        string  = "Total %d\n" % self.office_area;
        string += "Unallocated %d\n" % self.unallocated_area;
        string += "Contested %d\n" % self.contested_area;

        # Now, print guaranteed area for each employee
        for (name, area) in self.guaranteed_area.items():
            string += name + " " + str(area) + '\n';

        return string;



def read_cases_from_file(File):
    """ This method reads in cases from File. It appends each case (as a case
    type object) to a list of cases. The finished list is then returned.

    File is assumed to use the format specified by the problem statement."""
    case_list = [];

    # keep looping until we reach the end of the file
    while True:
        Office_Size_string = File.readline().strip();
        Office_Size_string = Office_Size_string.replace("\n","");

        # Check if Office_Size_string is empty (indiciating end of file)
        if(Office_Size_string == ""):
            break;

        Office_Size = Office_Size_string.split(" ");
        w = int(Office_Size[0]);
        h = int(Office_Size[1]);

        # Now, read in the number of cubicle requests
        num_cubicle_requests = int(File.readline());
        cubicle_requests = {};
        for i in range(num_cubicle_requests):
            # read in the ith cubicle request. turn this into a rectangle/name
            # pair and then append that pair to the cubicle_requests dictionary
            request = File.readline().replace("\n","").split(" ");
            name = request[0];
            cubicle = Rectangle(int(request[1]), int(request[2]), int(request[3]), int(request[4]));
            cubicle_requests[name] = cubicle;

        case_list.append(Case(h,w,cubicle_requests));

    return case_list;



def main():
    # Open the office.txt file and read in the cases
    File = open("office.txt","r");
    cases = read_cases_from_file(File);

    # Now, print out the cases
    for case in cases:
        print(case);

if (__name__ == "__main__"):
    main();
