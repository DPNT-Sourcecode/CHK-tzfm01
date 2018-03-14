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
        self.assertEqual(checkout("AA"), 50)

    def test_checkout_B(self):
        self.assertEqual(checkout("B"), 30)

if __name__ == '__main__':
    unittest.main()
