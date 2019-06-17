# Closed interval class
class Interval(object):
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
    def intersection(self, other):
        """This method finds the intersection of two intervals. If the
        intersection is non-empty then it is returned (as an interval).
        Otherwise, if the intersection is empty, then none is returned.

        let [a1, b1] , [a2, b2] be two intervals. They intersect as long as
        max(a1, a2) <= min(b1, b2). """
        a = max(self.a, other.a);
        b = min(self.b, other.b);

        if(a <= b):
            return Interval(a,b);
        else:
            return None;

    ############################################################################
    # Special methods

    def __str__(self):
        return "[%f, %f]" % (float(self.a), float(self.b));

    def __eq__(self, other):
        return (self.a == other.a) and (self.b == other.b);

    def __ne__(self, other):
        return not (self == other);
