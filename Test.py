import unittest;
from OfficeSpace import Interval, Rectangle

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



def main():
  unittest.main();

if (__name__ == "__main__"):
    main();
