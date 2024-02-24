import unittest
from main import playing_domino

class TestPlayingDomino(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]), [3, 4])

    def test_case_2(self):
        self.assertEqual(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]), [6, 5])

    def test_case_3(self):
        self.assertEqual(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]), [])

if __name__ == "__main__":
    unittest.main()