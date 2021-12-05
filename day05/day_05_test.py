import unittest

import day05.vents as vents


INPUTS = [
    '0,9 -> 5,9',
    '8,0 -> 0,8',
    '9,4 -> 3,4',
    '2,2 -> 2,1',
    '7,0 -> 7,4',
    '6,4 -> 2,0',
    '0,9 -> 2,9',
    '3,4 -> 1,4',
    '0,0 -> 8,8',
    '5,5 -> 8,2',
]


class Day05Test(unittest.TestCase):

  def test_test_case(self):
    lines = vents.parse_lines(INPUTS)

    points = vents.get_points_with_strength_at_least(lines, 2)

    self.assertEqual(5, len(points))
