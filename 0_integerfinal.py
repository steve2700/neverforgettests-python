#Write a function that adds 2 integers.

#Prototype: def add_integer(a, b=98):
#a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
#a and b must be first casted to integers if they are float
#Returns an integer: the addition of a and b
#You are not allowed to import any module


import unittest


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must an integer")
    a = int(a)
    b = int(b)
    return a + b

class TestAddIntegers(unittest.TestCase):

    def test_add_integer_with_integer(self):
        result = add_integer(5, 6)
        self.assertEqual(result, 11)

    def test_add_integer_with_floats(self):
        result = add_integer(1.0, 2.0)
        self.assertEqaul(result, 3)

    def test_add_integer_with_default_values(self):
        result = add_integer(1)
        self.assertEqual(result, 99)

    def test_add_integer_with_non_integers(self):
        with self.assertRaises(TypeError)
        add_integer("a","b")


if __name__ == '__main__':
    unittest.main()


