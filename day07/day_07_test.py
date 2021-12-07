import unittest

import day07.crabs as crabs


positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


class Day07Test(unittest.TestCase):

  def test_get_position_score(self):
    with self.subTest(2):
      self.assertEqual(37, crabs.get_position_score(positions, 2))
    with self.subTest(1):
      self.assertEqual(41, crabs.get_position_score(positions, 1))
    with self.subTest(3):
      self.assertEqual(39, crabs.get_position_score(positions, 3))
    with self.subTest(10):
      self.assertEqual(71, crabs.get_position_score(positions, 10))

  def test(self):
    self.assertEqual((2, 37), crabs.find_optimal_position(positions))
