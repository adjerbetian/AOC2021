import unittest

import day07.crabs1 as crabs1
import day07.crabs2 as crabs2


positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


class Day07Test(unittest.TestCase):

  def test_part_1_get_position_score(self):
    with self.subTest(2):
      self.assertEqual(37, crabs1.get_position_score(positions, 2))
    with self.subTest(1):
      self.assertEqual(41, crabs1.get_position_score(positions, 1))
    with self.subTest(3):
      self.assertEqual(39, crabs1.get_position_score(positions, 3))
    with self.subTest(10):
      self.assertEqual(71, crabs1.get_position_score(positions, 10))

  def test_part_1_optimal_position(self):
    self.assertEqual((2, 37), crabs1.find_optimal_position(positions))

  def test_part_2_get_position_score(self):
    with self.subTest(2):
      self.assertEqual(206, crabs2.get_position_score(positions, 2))
    with self.subTest(5):
      self.assertEqual(168, crabs2.get_position_score(positions, 5))

  def test_part_2_optimal_position(self):
    self.assertEqual((5, 168), crabs2.find_optimal_position(positions))
