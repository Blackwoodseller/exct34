import unittest

from p3 import primelist


class Testprimelist(unittest.TestCase):

    def test_1(self):
        # make sure primelist(1) returns list with single element
        self.assertEqual(primelist(1), [1])

    def test_2(self):
        # make sure primelist(2) returns list with two first prime numbers
        self.assertEqual(primelist(2), [1, 2])

    def test_100(self):
        # make sure primelist(2) returns list with 100 first prime numbers
        self.assertEqual(primelist(100), [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                                      73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
                                      157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
                                      239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                                      331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
                                      421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
                                      509, 521, 523])
        # make sure primelist(100) returns list with 100 elements
        self.assertEqual(len(primelist(100)), 100)


    def test_zero_amount(self):
        # make sure primelist(0) returns empty list
        self.assertEqual(primelist(0), [])

    def test_negative_parameter(self):
        # make sure primelist with negative parameter returns empty list
        self.assertEqual(primelist(-10), [])


if __name__ == '__main__':
    unittest.main()