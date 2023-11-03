import sys
import unittest
from importlib.machinery import SourceFileLoader
sys.path.append(r'C:\Users\marki\PycharmProjects\pyt_lab\lab\1')
calculator = SourceFileLoader('calculator', r'C:\Users\marki\PycharmProjects\pyt_lab\lab\1\calculator.py').load_module()


class CalculatorTesting(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(3, 1), 4)
        self.assertEqual(calculator.add(-10, 4.4), -5.6)
        self.assertEqual(calculator.add(-9.3, 0), -9.3)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(12, 30), -18)
        self.assertEqual(calculator.subtract(-11, 11), -22)
        self.assertEqual(calculator.subtract(-8, -8), 0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(22, 2), 44)
        self.assertEqual(calculator.multiply(-2, -2), 4)
        self.assertEqual(calculator.multiply(1, -1), -1)
        self.assertEqual(calculator.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(calculator.divide(12,4), 3)
        self.assertEqual(calculator.divide(-5, 1), -5)

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            calculator.add("hello", "yara")
        with self.assertRaises(TypeError):
            calculator.subtract(1, "-")
        with self.assertRaises(TypeError):
            calculator.multiply("hi", "12")
        with self.assertRaises(ArithmeticError):
            calculator.divide(11, 0)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(1, 0)
        with self.assertRaises(TypeError):
            calculator.divide(3, "hello")


if __name__ == '__main__':
    unittest.main()
