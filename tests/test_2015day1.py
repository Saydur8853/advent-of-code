import unittest

from year2015.solutions.day1 import part_1

class TestDay1(unittest.TestCase):
    def test_part_1(self):
        filename = "year2015/inputs/day1.e.txt"
        result = part_1(filename)
        self.assertEqual(result, 3)

    def test_run_part_1(self):
        filename = "year2015/inputs/day1.txt"
        result = part_1(filename)
        # print(result)
        self.assertEqual(1, 1, msg=f"{result}")