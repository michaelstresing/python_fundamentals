'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''

from math import sqrt
import unittest


def pythag(a, b):
    c1 = a ** 2 + b ** 2
    c = sqrt(c1)
    return c


print(pythag(3, 4))


class Testpythag(unittest.TestCase):

    def test_pythag(self):
        self.assertEqual(pythag(3, 4), 5)
        self.assertAlmostEquals(pythag(1, 1), 1.414214)
        self.assertEqual(pythag(0, 0), 0)
        self.assertEqual(pythag(-2, 0), 2)


if __name__ == '__main__':
    unittest.main()