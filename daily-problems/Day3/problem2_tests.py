import unittest

from problem2 import numSubarrayBoundedMax

class TestProblem2(unittest.TestCase):
    
    def tests(self):
        self.assertEqual(numSubarrayBoundedMax([2, 1, 4, 3], 2, 3), 3)
        self.assertEqual(numSubarrayBoundedMax([2, 9, 2, 5, 6], 2, 8), 7)
        self.assertEqual(numSubarrayBoundedMax([2, 2, 2, 2], 1, 3), 16)
        self.assertEqual(numSubarrayBoundedMax([1, 1, 1, 1, 1], 2, 3), 0)

unittest.main()
