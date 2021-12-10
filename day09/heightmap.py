from typing import Iterable

Position = tuple[int, int]


class Heightmap:
  def __init__(self, heights: list[list[int]]):
    self.heights = heights
    self.n = len(heights)
    self.m = len(heights[0])

  def get_risk_level(self) -> int:
    return sum(
        self.get_risk_level_at(position)
        for position in self.iter_positions()
        if self.is_low_point(position)
    )

  def get_risk_level_at(self, position: Position) -> int:
    return 1 + self[position]

  def is_low_point(self, position: Position) -> bool:
    value = self[position]
    return all(
        value < self[neighbour]
        for neighbour in self.iter_neighbours(position)
    )

  def iter_neighbours(self, position: Position) -> Iterable[Position]:
    for i in range(position[0] - 1, position[0] + 2):
      if i < 0 or i >= self.n: continue
      for j in range(position[1] - 1, position[1] + 2):
        if j < 0 or j >= self.m: continue
        if (i, j) == position: continue
        yield i, j

  def iter_cross_neighbours(self, position: Position) -> Iterable[Position]:
    if position[0] > 0:
      yield position[0] - 1, position[1]
    if position[0] < self.n - 1:
      yield position[0] + 1, position[1]
    if position[1] > 0:
      yield position[0], position[1] - 1
    if position[1] < self.m - 1:
      yield position[0], position[1] + 1

  def iter_positions(self) -> Iterable[Position]:
    for i in range(self.n):
      for j in range(self.m):
        yield i, j

  def __getitem__(self, position: Position) -> int:
    return self.heights[position[0]][position[1]]

  def get_basins(self) -> list[set[Position]]:
    return [
        self.get_basin(position)
        for position in self.iter_positions()
        if self.is_low_point(position)
    ]

  def get_basin(self, low_point: Position) -> set[Position]:
    visited = set[Position]()
    to_visit = set[Position]()
    to_visit.add(low_point)
    while len(to_visit) > 0:
      new_to_visit = set[Position]()
      for position in to_visit:
        for neighbour in self.iter_cross_neighbours(position):
          if neighbour in to_visit: continue
          if neighbour in visited: continue
          if self[neighbour] == 9: continue
          new_to_visit.add(neighbour)
        visited.add(position)
      to_visit = new_to_visit
    return visited
