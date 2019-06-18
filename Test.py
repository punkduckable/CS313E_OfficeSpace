from RectangleOverlap import Interval, Interval_Union;
import unittest;

# Interval tests.
class Interval_Tests(unittest.TestCase):
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

    def test_length(self):
        I1 = Interval(2,3);
        self.assertEqual(len(I1), 1);


# Interval Union tests.
class Interval_Union_Tests(unittest.TestCase):
    def test_append(self):
        U = Interval_Union();

        I1 = Interval(0,2);
        I2 = Interval(1,3);
        I3 = Interval(3,5);
        I4 = Interval(10,12);

        U.append(I1);
        U.append(I2);
        U.append(I3);
        U.append(I4);

        # Based on these three intervals, their union should be two intervals,
        # [0,5] and [10,12], with a total length of 7. First, lets check the
        # lenght
        self.assertEqual(len(U), 7);

        # Next, let's make sure that U's Interval list contains 2 elements.
        self.assertEqual(len(U.Interval_List),2);

        # Finally, let's check that the two intervals in the Interval List are
        # indeed [0,5] and [10,12].
        self.assertIn(Interval(0,5), U.Interval_List);
        self.assertIn(Interval(10,12), U.Interval_List);


if(__name__ == "__main__"):
    unittest.main();
