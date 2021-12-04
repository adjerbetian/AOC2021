from day04.board import Board


def get_first_winner_score(
    boards: list[Board],
    numbers_to_draw: list[int],
) -> Board:
  for n in numbers_to_draw:
    _mark_in_all(boards, n)
    if winner := _get_winner(boards):
      return winner.get_score(n)


def _mark_in_all(boards: list[Board], n: int):
  for board in boards:
    board.mark(n)


def _get_winner(boards: list[Board]) -> Board | None:
  for board in boards:
    if board.has_won():
      return board


def get_last_winner_score(
    boards: list[Board],
    numbers_to_draw: list[int],
) -> int:
  for n in numbers_to_draw:
    _mark_in_all(boards, n)
    if len(boards) == 1 and boards[0].has_won():
      return boards[0].get_score(n)
    boards = [board for board in boards if not board.has_won()]
  raise ValueError('No single last winner')
