import unittest

class AddTest(unittest.TestCase):
    def test_add(self):
        result = add(10, 5)
        expected = 15
        self.assertEqual(result, expected)

class SubtractTest(unittest.TestCase):
    def test_subtract(self):
        result = subtract(10, 5)
        expected = 5
        self.assertEqual(result, expected)

class MultiplyTest(unittest.TestCase):
    def test_multiply(self):
        result = multiply(10, 5)
        expected = 50
        self.assertEqual(result, expected)

class DivideTest(unittest.TestCase):
    def test_divide(self):
        result = divide(10, 5)
        expected = 2
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main