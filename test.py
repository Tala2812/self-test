
import unittest
from main import divide, modulo

class TestDivide(unittest.TestCase):
    def test_divide_success(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(70, 2), 35)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 6, 0)

class TestModulo(unittest.TestCase):
    def test_modulo_success(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(6, 4), 2)
        self.assertEqual(modulo(70, 7), 0)

    def test_modulo_by_zero(self):
        self.assertRaises(ValueError, modulo, 6, 0)

if __name__ == '__main__':
    unittest.main()