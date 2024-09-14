import unittest
from math import pi, sqrt, pow, hypot

class TestBuiltInFunctions(unittest.TestCase):

    def test_filter(self):
        result = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
        self.assertEqual(result, [2, 4, 6])

    def test_map(self):
        result = list(map(lambda x: x * 2, [1, 2, 3, 4]))
        self.assertEqual(result, [2, 4, 6, 8])

    def test_sorted(self):
        result = sorted([3, 1, 4, 2])
        self.assertEqual(result, [1, 2, 3, 4])
        result_reverse = sorted([3, 1, 4, 2], reverse=True)
        self.assertEqual(result_reverse, [4, 3, 2, 1])

### Тесты для функций из библиотеки math

    def test_pi(self):
        self.assertEqual(pi, 3.141592653589793)

    def test_sqrt(self):
        self.assertEqual(sqrt(16), 4)
        self.assertAlmostEqual(sqrt(2), 1.41421, places=5)

    def test_pow(self):
        self.assertEqual(pow(2, 3), 8)
        self.assertEqual(pow(3, 2), 9)

    def test_hypot(self):
        self.assertEqual(hypot(3, 4), 5)
        self.assertAlmostEqual(hypot(1, 1), 1.41421, places=5)


if __name__ == '__main__':
    unittest.main()
