import unittest
from main import find_min_and_max

class TestFindMinAndMax(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(find_min_and_max([]))

    def test_positive_numbers(self):
        self.assertEqual(find_min_and_max([5, 7, 4, -2, -1, 8]), "min: -2 index: 3 max: 8 index: 5")

    def test_mixed_numbers(self):
        self.assertEqual(find_min_and_max([2, -5, -4, 22, 7, 7]), "min: -5 index: 1 max: 22 index: 3")

    def test_negative_numbers(self):
        self.assertEqual(find_min_and_max([4, 3, 9, 4, -21, 7]), "min: -21 index: 4 max: 9 index: 2")

    def test_mixed_positive_and_negative_numbers(self):
        self.assertEqual(find_min_and_max([-1, 5, 6, 4, 2, 18]), "min: -1 index: 0 max: 18 index: 5")

    def test_negative_numbers_with_zero(self):
        self.assertEqual(find_min_and_max([-2, 5, -7, 4, 7, -20]), "min: -20 index: 5 max: 7 index: 4")

if __name__ == "__main__":
    unittest.main()