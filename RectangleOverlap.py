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

    def __len__(self):
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

    #############################################################################
    # special member functions
    def __len__(self):
        sum = 0;
        for i in range(len(self.Interval_List)):
            sum += len(self.Interval_List[i]);

        return sum;
