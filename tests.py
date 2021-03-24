# tests.py

import random
try:
    import unittest2 as unittest
except ImportError:
    import unittest

class SimpleTest(unittest.TestCase):

    def test_pass1(self):
        self.assertEqual(10, 7 + 3)

    def test_pass2(self):
        self.assertEqual(100, 10 * 10)

    #def test_fail1(self):
    #    self.assertEqual(11, 7 + 3)

if __name__ == '__main__':
    unittest.main()
