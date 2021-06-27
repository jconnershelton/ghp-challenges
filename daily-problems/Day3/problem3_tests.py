import unittest

from problem3 import numSubarrayBoundedMax

class TestProblem2(unittest.TestCase):
    
    def tests(self):
        return self.assertEqual(numSubarrayBoundedMax([2, 1, 4, 3], 2, 3), 3)
        
