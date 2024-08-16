import unittest

from classFraction import *


class EqualTest(unittest.TestCase):

    def test_eq(self):
        self.assertEqual(Fraction(1, 2) == Fraction(1, 2), True, "True")
        self.assertEqual(Fraction(46, 2) == Fraction(46, 2), True, "True")
        self.assertEqual(Fraction(17, 14) == Fraction(17, 1), False, "True")

    def test_eq_str(self):
        self.assertRaises(TypeError, Fraction(1, 2) == "bonjour")
        self.assertRaises(TypeError, Fraction(1, 2) == "bonsoir")

    def test_eq_int_float(self):
        self.assertEqual(Fraction(1, 2) == 0.5, True, "True")
        self.assertEqual(Fraction(1, 4) == 0.5, False, "False")


class MulTest(unittest.TestCase):

    def test_mul(self):
        self.assertEqual(Fraction(1, 2) * Fraction(1, 2), Fraction(1, 4), "Fraction(1,4)")
        self.assertEqual(Fraction(5, 2) * Fraction(2, 8), Fraction(5, 8), "Fraction(5,8)")

    def test_mul_errors(self):
        self.assertRaises(TypeError, Fraction(1, 4) * "bonjour")
        self.assertRaises(TypeError, Fraction(1, 4) * "super")

    def test_mul_float(self):
        self.assertEqual(Fraction(1, 2) * 2, 1, "1")
        self.assertEqual(Fraction(1, 2) * 10, 5, "5")
        #self.assertEqual(Fraction(1, 2) * 0.5, 0.25, "0.25")


class PowTest(unittest.TestCase):

    #def test_pow(self):
       # self.assertEqual(Fraction(1, 2) ** Fraction(2, 1), Fraction(1, 4), "0.707")

    def test_pow_int(self):
        self.assertEqual(Fraction(1, 2) ** 2, Fraction(1, 4), "Fraction(1,4)")
        self.assertEqual(Fraction(2, 5) ** 4, Fraction(16, 625), "Fraction(16,625)")

    def test_pow_errors(self):
        self.assertRaises(TypeError, Fraction(1, 2) ** "bonjour")
        self.assertRaises(TypeError, Fraction(2, 5) ** "bonsoir")


class test_as_mixed_number(unittest.TestCase):
    """def test_init(self):
        self.assertRaises(Fraction(1, 0),fraction_implémenté.ValueZero, "Fraction(1, 0)")"""

    def test_as_mixed_number(self):
        self.assertEqual(Fraction(1, 2) + 2, Fraction(5,2), "Fraction(1, 2) + 2")
        self.assertEqual(Fraction(1, 2) + 0, Fraction(1,2), "Fraction(1, 2) + 0")
        self.assertEqual(Fraction(1, 2) - 2, Fraction(-3,2), "Fraction(1, 2) - 2")

    def test_raises_as_mixed_number(self):
        self.assertRaises(TypeError, Fraction(1, 2) + "lidel", "Fraction(1, 2) + lidel")
        self.assertRaises(TypeError, Fraction(1, 2) + [], "Fraction(1, 2) + lidel")


class test_add(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Fraction(1, 2) + Fraction(1, 2), 1, "Fraction(1, 2) + Fraction(1, 2)")
        self.assertEqual(Fraction(1, 2) + Fraction(-1, 2), 0, "Fraction(1, 2) + Fraction(-1, 2)")
        self.assertEqual(Fraction(1, 2) + 1, 3 / 2, "Fraction(1, 2) - Fraction(1, 2)")

    def test_raises_add(self):
        self.assertRaises(TypeError, Fraction(1, 2) + "lidel", "Fraction(1, 2) + lidel")
        self.assertRaises(TypeError, Fraction(1, 2) + [], "Fraction(1, 2) + lidel")


class test_sub(unittest.TestCase):
    def test_sub(self):
        self.assertEqual(Fraction(1, 2) - Fraction(1, 2), 0, "Fraction(1, 2) + Fraction(1, 2)")
        self.assertEqual(Fraction(1, 2) - 1, Fraction(-1,2), "Fraction(1, 2) + Fraction(1, 2)")

    def test_raises_sub(self):
        self.assertRaises(TypeError, Fraction(1, 2) - "lidel", "Fraction(1, 2) + lidel")
        self.assertRaises(TypeError, Fraction(1, 2) - [], "Fraction(1, 2) + lidel")


class test_true_div(unittest.TestCase):
    def test_true_div(self):
        self.assertEqual(Fraction(4, 4) / Fraction(1, 2), 2, "Fraction(4, 4)/Fraction(1, 2)")
        #self.assertEqual(Fraction(4, 4) / 0.5, 2, "Fraction(4, 4) / 0.5")
        self.assertEqual(Fraction(4, 4) / 2, 0.5, "Fraction(4, 4) / 2")

    def test_raises_true_div(self):
        self.assertRaises(TypeError, Fraction(1, 2) / "lidel", "Fraction(1, 2) / lidel")
        self.assertRaises(TypeError, Fraction(1, 2) / [], "Fraction(1, 2) / []")


class test_float(unittest.TestCase):
    def test_float(self):
        self.assertEqual(float(Fraction(1, 2)), 0.5, "float(Fraction(1, 2)")
        self.assertEqual(float(Fraction(0, 4)), 0, "float(Fraction(0, 4))")


class test_is_zero(unittest.TestCase):
    def test_is_zero(self):
        self.assertEqual(Fraction(0, 2).is_zero(), True, "Fraction(0, 2).is_zero()")
        self.assertEqual(Fraction(1, 4).is_zero(), False, "Fraction(1, 4).is_zero()")


class test_is_integer(unittest.TestCase):
    def test_is_zero(self):
        self.assertEqual(Fraction(4, 2).is_integer(), True, "Fraction(4, 2).is_integer()")
        self.assertEqual(Fraction(1, 3).is_integer(), False, "Fraction(1, 3).is_integer()")


class test_is_proper(unittest.TestCase):
    def test_is_proper(self):
        self.assertEqual(Fraction(4, 2).is_proper(), False, "float(Fraction(1, 2)")
        self.assertEqual(Fraction(-1, 2).is_proper(), True, "float(Fraction(1, 2)")
        self.assertEqual(Fraction(1, 2).is_proper(), True, "float(Fraction(1, 2)")


class test_is_unit(unittest.TestCase):
    def test_is_unit(self):
        self.assertEqual(Fraction(2, 3).is_unit(), False, "Fraction(2, 3).is_unit()")
        self.assertEqual(Fraction(2, 4).is_unit(), True, "Fraction(4, 2).is_unit()")


class test_is_adjacent_to(unittest.TestCase):
    def test_is_adjacent_to(self):
        self.assertEqual(Fraction(2, 1).is_adjacent_to(Fraction(1, 1)), True, "Fraction(2, 3).is_unit()")
        self.assertEqual(Fraction(2, 4).is_adjacent_to(Fraction(2, 3)), False, "Fraction(4, 2).is_unit()")

    def test_raises_is_adjacent_to(self):
        self.assertRaises(TypeError, Fraction(2, 1).is_adjacent_to("lidel"), "Fraction(2, 1).is_adjacent_to(lidel)")
        self.assertRaises(TypeError, Fraction(2, 1).is_adjacent_to([]), "Fraction(2, 1).is_adjacent_to([])")


if __name__ == '__main__':
    unittest.main()
