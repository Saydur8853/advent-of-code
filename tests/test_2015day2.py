import unittest

from year2015.solutions.day2 import part_1

class TestDay2(unittest.TestCase):
    def test_part_1(self):
        filename = "year2015/inputs/day2.e.txt"
        result = part_1(filename)
        self.assertEqual(result, 3)

    def test_run_part_1(self):
        filename = "year2015/inputs/day2.txt"
        result = part_1(filename)
        # print(result)
        self.assertEqual(1, 1, msg=f"{result}")