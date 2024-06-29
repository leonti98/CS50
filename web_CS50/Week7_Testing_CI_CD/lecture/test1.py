import unittest

from prime import is_prime


class Test(unittest.TestCase):

    def test_1(self):
        """Check is 1 is not prime"""
        self.assertFalse(is_prime(1))

    def test_2(self):
        """Check is 2 is prime"""
        self.assertTrue(is_prime(2))

    def test_8(self):
        """Check is 8 is not prime"""
        self.assertFalse(is_prime(8))

    def test_11(self):
        """Check is 11 is prime"""
        self.assertTrue(is_prime(11))

    def test_25(self):
        """check 25 is not prime"""
        self.assertFalse(is_prime(25))

    def test_28(self):
        """check 28 is not prime"""
        self.assertFalse(is_prime(28))


if __name__ == "__main__":
    unittest.main()
