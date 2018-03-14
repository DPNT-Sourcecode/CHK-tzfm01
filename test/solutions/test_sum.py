import unittest

from lib.solutions.sum import sum
from lib.solutions.hello import hello


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello('Mihai'), 'Hello, Mihai!')


if __name__ == '__main__':
    unittest.main()
