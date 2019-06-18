import unittest;
from OfficeSpace import Interval, Rectangle, Case

class Interval_Tests(unittest.TestCase):
    def test_length(self):
        # Test with integer coordinates
        I1 = Interval(1,3);
        self.assertEqual(I1.length(), 2);

        # Test with floating point coordinates
        I2 = Interval(-2.7,2.1);
        self.assertEqual(I2.length(), (2.1+2.7));

    def test_contains(self):
        I1 = Interval(0,2);
        self.assertNotIn(-1.1, I1);
        self.assertIn(0, I1);
        self.assertIn(1.7, I1);
        self.assertIn(2, I1);
        self.assertNotIn(2.1, I1);



class Rectangle_Tests(unittest.TestCase):
    def test_area(self):
        # Test with integer coordinates
        R1 = Rectangle(0,0,1,1);
        self.assertEqual(R1.area(),1);

        # Test with floating point coordinates
        R2 = Rectangle(.1, .1, 1.1, 1.1);
        self.assertEqual(R2.area(), 1);

    def test_contains(self):
        R1 = Rectangle(0,0,1,1);

        self.assertNotIn((-.1, .5), R1);
        self.assertIn((0,0), R1);
        self.assertIn((.5,.5), R1);
        self.assertIn((1,0), R1);
        self.assertIn((1,1), R1);
        self.assertNotIn((.5, 1.1), R1);



class Case_Tests(unittest.TestCase):
    def test_init(self):
        h = 30;
        w = 50;
        cubicle_requests = {"Bob":Rectangle(1,1, 10, 10), "Jenny":Rectangle(30,10,50,30), "Blake":Rectangle(5, 0, 20, 20)};

        C1 = Case(h,w,cubicle_requests);
        self.assertEqual(C1.office_area, 1500);
        self.assertEqual(C1.unallocated_area, 764);
        self.assertEqual(C1.allocated_area, 736);
        self.assertEqual(C1.contested_area, 45)


def main():
  unittest.main();

if (__name__ == "__main__"):
    main();
