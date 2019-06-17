from OfficeSpace import Interval;
import unittest;

# Interval tests.
class IntervalTests(unittest.TestCase):
    def test_equal(self):
        I1 = Interval(0,1);
        I2 = Interval(0,1);
        self.assertEqual(I1, I2);

        I3 = Interval(1,2);
        self.assertNotEqual(I1,I3);

    def test_intersection_interval(self):
        I1 = Interval(0,1);
        I2 = Interval(0,2);
        # The intersection of [0,1] and [0,2] should be [0,1]
        self.assertEqual(I1.intersection(I2), Interval(0,1));

        I3 = Interval(1,2);
        # Intersection of [0,1] and [1,2] should be the interval [1,1]
        self.assertEqual(I1.intersection(I3), Interval(1,1));

        I4 = Interval(2,3);
        # The intersection of [0,1] and [2,3] should be the empty set (None)
        self.assertIsNone(I1.intersection(I4));

if(__name__ == "__main__"):
    unittest.main();
