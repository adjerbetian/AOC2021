import unittest

import day09.heightmap as heightmap


class Day09Test(unittest.TestCase):

  def test_get_first_wrong_character(self):
    hm = heightmap.Heightmap([
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ])

    self.assertEqual(15, hm.get_risk_level())

  def test_is_low_point(self):
    hm = heightmap.Heightmap([
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ])

    self.assertTrue(hm.is_low_point((0, 1)))
    self.assertTrue(hm.is_low_point((2, 2)))
    self.assertTrue(hm.is_low_point((4, 6)))

    self.assertFalse(hm.is_low_point((0, 0)))
    self.assertFalse(hm.is_low_point((1, 0)))
    self.assertFalse(hm.is_low_point((2, 5)))
