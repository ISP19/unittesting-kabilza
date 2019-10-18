import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        f = Fraction(99)
        self.assertEqual("99", f.__str__())


    def test_init(self):
        with self.assertRaises(NameError):
            Fraction(abc,der)
        with self.assertRaises(NameError):
            Fraction(erw,vfe)
        f = Fraction(2,3)
        self.assertEqual(3, f.denominator)
        f = Fraction(4,5)
        self.assertEqual(5, f.denominator)
        f = Fraction(10,3)
        self.assertEqual(3, f.denominator)
        f = Fraction(99,20)
        self.assertEqual(99, f.numerator)
        f = Fraction(1,1)
        self.assertEqual(1, f.denominator)
        f = Fraction(2,-3)
        self.assertEqual(-2, f.numerator)

    def test_multiply(self):
        with self.assertRaises(TypeError):
            Fraction('ab','cd')
        with self.assertRaises(TypeError):
            Fraction('wdfwef','er')
        self.assertEqual(Fraction(9,16), Fraction(3,4)*Fraction(3,4))
        self.assertEqual(Fraction(8,9), Fraction(2,3)*Fraction(4,3))
        self.assertEqual(Fraction(1,2), Fraction(9,9)*Fraction(1,2))
        self.assertEqual(Fraction(9,16), Fraction(3,4)*Fraction(3,4))
        self.assertEqual(Fraction(72,91), Fraction(12,13)*Fraction(12,14))
        self.assertEqual(Fraction(1,2), Fraction(4,4)*Fraction(2,4))

    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))
        self.assertEqual(Fraction(5,4), Fraction(5,8)+Fraction(5,8))
        self.assertEqual(Fraction(7,4), Fraction(6,6)+Fraction(3,4))
        self.assertEqual(Fraction(7,2), Fraction(3,2)+Fraction(2,1))
        self.assertEqual(Fraction(8,3), Fraction(6,3)+Fraction(2,3))
        self.assertEqual(Fraction(14,5), Fraction(2,2)+Fraction(9,5))
        self.assertEqual(Fraction(0,0), Fraction(0,5)+Fraction(5,0))
        

    def test_subself(self):
        # -7/12 = 1/2 - 2/3
        self.assertEqual(Fraction(-7,12), Fraction(1,12)-Fraction(2,3))
        self.assertEqual(Fraction(4,3), Fraction(6,3)-Fraction(2,3))
        self.assertEqual(Fraction(-7,5), Fraction(2,5)-Fraction(9,5))
        self.assertEqual(Fraction(0,0), Fraction(0,5)-Fraction(5,0))
        self.assertEqual(Fraction(0,8), Fraction(5,8)-Fraction(5,8))
        self.assertEqual(Fraction(6,24), Fraction(6,6)-Fraction(3,4))
        self.assertEqual(Fraction(-1,2), Fraction(3,2)-Fraction(2,1))
        

    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))

        a = Fraction(3,4)
        b = Fraction(9,16)
        c = Fraction(4,6)
        self.assertTrue(a == b)
        self.assertTrue(a.__eq__(b))
        self.assertFalse(a == c)
        self.assertFalse(a.__eq__(c))

        a = Fraction(30,90)
        b = Fraction(1,3)
        c = Fraction(89,23)
        self.assertTrue(a == b)
        self.assertTrue(a.__eq__(b))
        self.assertFalse(a == c)
        self.assertFalse(a.__eq__(c))

        a = Fraction(1,0)
        b = Fraction(-1,0)
        c = Fraction(0,0)
        self.assertTrue(a == b)
        self.assertTrue(a.__eq__(b))
        self.assertTrue(a == c)
        self.assertTrue(a.__eq__(c))

    def test_gt(self):
        a = Fraction(1,2)
        b = Fraction(2,3)
        self.assertTrue(a < b)
        self.assertFalse(b < a)

        c = Fraction(5,6)
        d = Fraction(6,6)
        self.assertTrue(c < d)
        self.assertFalse(d < c)

        c = Fraction(12,8)
        d = Fraction(4,6)
        self.assertFalse(c < d)
        self.assertTrue(d < c)

        c = Fraction(5,10)
        d = Fraction(1,2)
        self.assertFalse(c < d)
        self.assertFalse(d < c)
        #both of them are equal so the function returns False
        #for both attempts


if __name__ == "__main__":
    unittest.main(verbosity=2)