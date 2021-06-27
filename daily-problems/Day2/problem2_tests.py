import unittest

from problem2 import nextGreaterElements

class TestProblem2(unittest.TestCase):

    def tests(self):
        self.assertEqual(nextGreaterElements([1, 2, 1]), [2, -1, 2])
        self.assertEqual(nextGreaterElements([1, 2, 3, 4, 3]), [2, 3, 4, -1, 4])
        self.assertEqual(nextGreaterElements([13, 4, 9, 3, 2]), [-1, 9, 13, 13, 13])
        self.assertEqual(nextGreaterElements([1, 1, 1, 1]), [-1, -1, -1, -1])

unittest.main()

