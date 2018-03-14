import unittest

from lib.solutions.sum import sum
from lib.solutions.hello import hello
from lib.solutions.checkout import checkout


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello('Mihai'), 'Hello, Mihai!')


class TestCheckout(unittest.TestCase):
    def test_checkout_0(self):
        self.assertEqual(checkout(""), 0)

    def test_checkout_A(self):
        self.assertEqual(checkout("E"), 40)

    def test_checkout_B(self):
        self.assertEqual(checkout("ABCDEF"), 165)

if __name__ == '__main__':
    unittest.main()
