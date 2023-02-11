import unittest



class TestAddInteger(unittest.Testcases):


    def test_add_integer_with_integers(self):
        result = add_integer(1, 2)
        self.assertEqual(result, 3)

    def test_add_integer_with_floats(self):
        result = add_integer(2.0, 1.0)
        self.assertEqual(result, 3)
    def test_add_integer_with_default_value(self):
        result = add_integer(1)
        self.assertEqual(result, 99)
    def test_add_integer_with_non_integer_input(self):
        with self.assertRaises(TypeError)
        add_integer("a", "b")



if __name__ == '__main__':
    unittest.main()



