# Closed interval class
class Interval(object):
    """ This class models closed intervals """

    ############################################################################
    # Constructor
    def __init__(self, a, b):
        # make sure that a, b are in the correct order. If not, swap them.
        if(a > b):
            temp = a;
            a = b;
            b = temp;

        self.a = a;
        self.b = b;

    ############################################################################
    # Other methods

    def intersects(self, other):
        """ This method returns wheather or not self and other intersect.

        let [a1, b1] , [a2, b2] be two intervals. These intervals intersect as
        long as max(a1, a2) <= min(b1, b2) """
        a = max(self.a, other.a);
        b = min(self.b, other.b);

        if(a <= b):
            return True;
        else:
            return False;


    def intersection(self, other):
        """This method finds the intersection of two intervals. If the
        intersection is non-empty then it is returned (as an interval).
        Otherwise, if the intersection is empty, then none is returned.

        let [a1, b1] , [a2, b2] be two intervals. The two intervals intersect
        if max(a1, a2) <= min(b1, b2). In this case, their intersection is
        [max(a1,a2), min(b1, b2)] """
        a = max(self.a, other.a);
        b = min(self.b, other.b);

        if(a <= b):
            return Interval(a,b);
        else:
            return None;

    def length(self):
        return self.b - self.a;

    ############################################################################
    # Special methods

    def __str__(self):
        return "[%f, %f]" % (float(self.a), float(self.b));

    def __eq__(self, other):
        return (self.a == other.a) and (self.b == other.b);

    def __ne__(self, other):
        return not (self == other);



# Interval union class
# This class models the union of closed intervals. In general, the union of two
# closed intervals is not a closed interval. Thus, we have a separate class
# just to deal with this situation.
class Interval_Union(object):
    """an Interval_Union object contains a single data member,
    its Interval_List. This contains a set of non-intersecting closed intervals.
    since the intervals are non-overlapping, we can easily find the total
    length of the Interval_Union by summing up the lengths of the intervals
    in the Interval_List """

    ############################################################################
    # Constructor:
    def __init__(self):
        # Start off with an empty Interval_List.
        self.Interval_List = [];

    ############################################################################
    # append (and helper function(s))
    def _intersects_with_interval_in_list(self, I):
        # This method determines if the interval I intersects with any of the
        # intervals in intervals in the Interval_List. If so, then this function
        # returns the index of the first item in the Interval_List that
        # intersects with I. Otherwise, a -1 is returned.
        for i in range(len(self.Interval_List)):
            if(self.Interval_List[i].intersects(I)):
                return i;

        # If we get to here, then I does not intersect with any of the intervals
        # in the list, return -1.
        return -1;

    def append(self, I):
        # This method appends another interval, I, onto the Interval list.

        # First, we need to figure out if I intersects with any of the intervals
        # in the Interval list (see above).
        i = self._intersects_with_interval_in_list(I)
        if(i != -1):
            # If so, then we need to find the union of I with the ith
            # interval, remove the ith interval from the Interval List, and then
            # append the combined result onto self.
            ith_interval = self.Interval_List.pop(i);
            a = min(ith_interval.a, I.a);
            b = max(ith_interval.b, I.b);

            combined_interval = Interval(a,b);
            self.append(combined_interval);
        else:
            # if not, then I is disjoint from every interval in the Interval
            # List, we can safely append I onto the Interval List.
            self.Interval_List.append(I);

    def length(self):
        sum = 0;
        for i in range(len(self.Interval_List)):
            sum += self.Interval_List[i].length();

        return sum;

    ############################################################################
    # Special methods
    def __str__(self):
        str = ""
        num_intervals = len(self.Interval_List)
        for i in range(num_intervals-1):
            str += str(self.Interval_List[i]) + " and "

        str += self.Interval_List[num_intervals-1];
        return str;



# rectangle class
class Rectangle(object):
    # Constructor. ll_x/ll_y are the coordinates of the lower-left (south-west)
    # corner of the rectangle. ur_x/ur_y are the coordinates of the upper-right
    # (north east) coorner of the rectangle.
    def __init__(self, ll_x, ll_y, ur_x, ur_y):
        self.x_range = Interval(ll_x, ur_x);
        self.y_range = Interval(ll_y, ur_y);


    def area(self):
        return self.x_range.length()*self.y_range.length();

    # returns true if x is inside the x_range of self and the right edge of
    # self is to the right of x. This occurs whenever x is in [a,b) where
    # x_range = [a,b].
    def intersects_right(self, x):
        return (self.x_range.a <= x) and (x < self.x_range.b);

    # if x intersects and is not the right edge of self (if intersects_right(x)
    # is True) then this returns the interval of intersection (which is just
    # the y range of self). Otherwise it returns None.
    def intersection_right(self,x):
        if(self.intersects_right(x)):
            return self.y_range;
        else:
            return None;

    ############################################################################
    # Special methods
    def __str__(self):
        return str(self.x_range) + "x" + str(self.y_range);


def read_rectangles():
    # This function reads in a list of rectangles from Rectangles.txt. It then
    # writes these rectangles to a list and returns that list
    File = open("Rectangles.txt","r");

    # First, read in the number of rectangles
    num_recs = int(File.readline());

    # Now, read in each rectangle.
    Rectangles = [];
    for i in range(num_recs):
        # read in the line and space split it
        ith_rectangle_coords = File.readline().split(" ");
        ll_x = float(ith_rectangle_coords[0]);
        ll_y = float(ith_rectangle_coords[1]);
        ur_x = float(ith_rectangle_coords[2]);
        ur_y = float(ith_rectangle_coords[3]);

        Rectangles.append(Rectangle(ll_x, ll_y, ur_x, ur_y));

    return Rectangles;



def rectangles_right_intersection(Rectangles, x):
    """ This function first finds the right-intersection of the verticlal line x
    with the list of Rectangles. This is returned as an Interval Union object.

    We say that a rectangle right-intersects the vertical line x if x is in the
    x range of the rectangle and x is not the right edge of the rectangle.
    In other words, the vertical line x must intersect the rectangle and the
    rectangle must extend to the right of the vertical line x.

    for each rectangle that right-intersects x, we append the intersection
    interval onto a Interval_Union object. Once we have done this for each
    rectangle that right-intersects x, we return the Interval_Union object. """

    U = Interval_Union();
    for rec in Rectangles:
        if(rec.intersects_right(x)):
            U.append(rec.intersection_right(x));

    return U;



def main():
    """ Here we find the total area covered by the Rectangles in Rectangles.txt.
    To understand our approach, suppose that we want to find the area covered by
    the following rectangles,
    _______         ___________
    |     |         |  ____   |
    |   __|______   |  |  |   |
    |   | |     |   |  |  |   |
    |   | |     |   |  ----   |
    ----|       |   -----------
        ---------

    Seems tricky. However, let's consider what we would get if we were to
    "slice" the rectangles along a vertical line x = c. A little thought reveals
    that we would get the verical cross section of the rectangles at x = c. Now
    imagine what this cross section would look like as c moves left or right.
    you may notice that the cross section only changes when we hit the left or
    right edge of a rectangle.

    With these insights, we can derive a method to find the area covered by
    the rectangles. In particular, let Edges be the list of the x coordinates
    of the left and right edges of every rectangle. for simplicity, we will
    assume that Edges is sorted in ascending order. Notice that between
    Edges[i] and Edges[i+1], the vertical cross section is constant (since no
    rectangle begins or ends in that interval). As such, the area between
    Edge[i] and Edge[i+1] that is covered by the rectangles is just the length
    of the vertical cross section in that interval times Edge[i+1] - Edge[i].

    What is the length of the vertical cross section? Considering the picture
    below, we can see that the only rectangles that contribute to the area
    are those that exist to the right of Edge[i]. In other words, if a rectangle
    has its right edge at Edge[i], then it will not contribute to the vertical
    cross section between Edge[i] and Edge[i+1]. Thus, we first find the set of
    rectangles that exist between Edge[i] and Edge[i+1]. Next, we find the
    intersection of each one of these rectangles with the vertical line Edge[i].
    Next, we take the union of each of these intervals. Finally, we find
    the length of the union. That length is the length of the vertical cross
    section.

    If we do this for each i then we will have found the area of the rectangles.
    Visually, we're just splitting up the covered area along verticle lines
    through the left and right edges of the rectangles, then adding up the
    area of the rectangles between these slices.

    |   | |     |   |  |  |   |
    |___|_|     |   |__|__|___|
    |   | |     |   |  |__|   |
    |   |_|_____|   |  |  |   |
    |   | |     |   |  |  |   |
    |   | |     |   |  |--|   |
    |---| |     |   |--|--|---|
    |   |-|-----|   |  |  |   |
    |   | |     |   |  |  |   | """

    # First, read in the rectangles from the Rectangles.txt file
    Rectangles = read_rectangles();

    # collect the left and right ends of the rectangle into a set .
    edge_coords = set();
    for rec in Rectangles:
        edge_coords.add(rec.x_range.a);
        edge_coords.add(rec.x_range.b);

    # Now, convert the set into a list and sort it.
    sorted_edge_coords = sorted(list(edge_coords));

    # Now we can cycle through the x coordinates and use this to find the area
    # using the "sweep" method.
    area = 0;

    for i in range(len(sorted_edge_coords)-1):
        # Find the right-intersection of the vertical line x with Rectangles. A
        # rectangle right-intersects with the line x if x intersects with the
        # rectangle and x is not the right edge of the rectangle.
        U = rectangles_right_intersection(Rectangles, sorted_edge_coords[i]);

        area += U.length()*(sorted_edge_coords[i+1] - sorted_edge_coords[i]);

    print("The total area covered by the rectangles is %f" % area);



if(__name__ == "__main__"):
    main();
