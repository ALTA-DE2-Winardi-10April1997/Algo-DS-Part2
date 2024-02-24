import unittest
from main import maximum_buy_product

class TestMaximumBuyProduct(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(maximum_buy_product(50000, [25000, 25000, 10000, 14000]), 3)

    def test_case_2(self):
        self.assertEqual(maximum_buy_product(30000, [15000, 10000, 12000, 5000, 3000]), 4)

    def test_case_3(self):
        self.assertEqual(maximum_buy_product(10000, [2000, 3000, 1000, 2000, 10000]), 4)

    def test_case_4(self):
        self.assertEqual(maximum_buy_product(4000, [7500, 3000, 2500, 2000]), 1)

    def test_case_5(self):
        self.assertEqual(maximum_buy_product(0, [10000, 30000]), 0)

if __name__ == "__main__":
    unittest.main()