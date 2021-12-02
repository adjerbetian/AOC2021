import unittest

from day02.Submarine import Submarine
from day02.Instruction import parse_instructions

TEST_INSTRUCTIONS = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2',
]


class TestDay2(unittest.TestCase):

  def test_submarine_follows_instructions(self):
    instructions = parse_instructions(TEST_INSTRUCTIONS)
    submarine = Submarine()

    submarine.follow_instructions(instructions)

    self.assertEqual(submarine.x, 15)
    self.assertEqual(submarine.depth, 10)


if __name__ == '__main__':
  unittest.main()
