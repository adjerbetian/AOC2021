import unittest

import day06.lanternfish as lanternfish


class Day06Test(unittest.TestCase):

  def test_test_case(self):
    ages = [3, 4, 3, 1, 2]

    with self.subTest('after 18 days'):
      population = lanternfish.build_population(ages)

      population = lanternfish.pass_n_days(population, 18)

      self.assertEqual(26, lanternfish.get_population_count(population))

    with self.subTest('after 80 days'):
      population = lanternfish.build_population(ages)

      population = lanternfish.pass_n_days(population, 80)

      self.assertEqual(5934, lanternfish.get_population_count(population))
