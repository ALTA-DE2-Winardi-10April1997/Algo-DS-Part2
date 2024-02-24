import unittest
from main import count_item_and_sort

class TestCountItemAndSort(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]), "golang->1 ruby->2 js->4")

    def test_case_2(self):
        self.assertEqual(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]), "C->1 D->2 B->3 A->4")

    def test_case_3(self):
        self.assertEqual(count_item_and_sort(["football", "basketball", "tenis"]), "basketball->1 football->1 tenis->1")

if __name__ == "__main__":
    unittest.main()