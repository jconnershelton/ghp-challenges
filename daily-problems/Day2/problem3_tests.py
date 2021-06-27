import unittest

from problem3 import getMaxRepetitions

class TestProblem3(unittest.TestCase):

    def tests(self):
        self.assertEqual(getMaxRepetitions('acb', 4, 'ab', 2), 2)
        self.assertEqual(getMaxRepetitions('acb', 1, 'acb', 1), 1)
        self.assertEqual(getMaxRepetitions('xyz$3', 14, '27', 3), 0)
        self.assertEqual(getMaxRepetitions('a', 5, 'a', 2), 2)

unittest.main()

