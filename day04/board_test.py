import unittest

from day04.board import Board


class BoardTest(unittest.TestCase):

  def test_board_no_win(self):
    board = Board([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])

    self.assertFalse(board.has_won())

    board.mark(1)
    board.mark(2)
    board.mark(4)
    board.mark(5)

    self.assertFalse(board.has_won())

  def test_board_win_horizontal(self):
    board = Board([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])

    board.mark(1)
    board.mark(2)
    board.mark(3)

    self.assertTrue(board.has_won())

  def test_board_win_vertically(self):
    board = Board([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])

    board.mark(1)
    board.mark(4)
    board.mark(7)

    self.assertTrue(board.has_won())

  def test_board_score(self):
    board = Board([
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ])

    for n in [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24]:
      board.mark(n)

    self.assertEqual(4512, board.get_score(24))


if __name__ == '__main__':
  unittest.main()
