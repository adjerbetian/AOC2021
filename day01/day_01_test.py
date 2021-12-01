import unittest

from day01.day_01 import count_increases


TEST_DEPTHS = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]


class TestDay1(unittest.TestCase):

  def test_count_increases(self):
    result = count_increases(TEST_DEPTHS)
    self.assertEqual(7, result)

  def test_count_sliding_increases(self):
    result = count_increases(TEST_DEPTHS, window_size=3)
    self.assertEqual(5, result)


if __name__ == '__main__':
  unittest.main()
