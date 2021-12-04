Grid = list[list[int]]


class Board:
  def __init__(self, grid: Grid):
    self.n = len(grid)
    self.grid = grid
    self.marked = [
        [False] * self.n
        for _ in range(self.n)
    ]

  def mark(self, number: int):
    for i in range(self.n):
      for j in range(self.n):
        if self.grid[i][j] == number:
          self.marked[i][j] = True

  def has_won(self) -> bool:
    return self._has_won_horizontally() or self._has_won_vertically()

  def _has_won_horizontally(self) -> bool:
    for i in range(self.n):
      if all(self._get_marked_row(i)):
        return True
    return False

  def _has_won_vertically(self) -> bool:
    for j in range(self.n):
      if all(self._get_marked_column(j)):
        return True
    return False

  def _get_marked_row(self, i: int) -> list[bool]:
    return self.marked[i]

  def _get_marked_column(self, j: int) -> list[bool]:
    return [self.marked[i][j] for i in range(self.n)]

  def get_score(self, last_drawn: int):
    return last_drawn * sum(
        self.grid[i][j]
        for i in range(self.n)
        for j in range(self.n)
        if not self.marked[i][j]
    )

  def __str__(self) -> str:
    return '\n'.join(
        ' '.join(
            f'{self.grid[i][j]:>2}' if not self.marked[i][j] else ' X'
            for j in range(self.n)
        )
        for i in range(self.n)
    )
