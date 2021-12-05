import dataclasses
import itertools
from collections import defaultdict
from typing import Iterator

Point = tuple[int, int]


@dataclasses.dataclass
class Line:
  origin: Point
  destination: Point

  def __str__(self):
    return f'{self.origin} -> {self.destination}'


def get_points_with_strength_at_least(
    lines: list[Line],
    minimum_strength: int,
) -> list[Point]:
  points = defaultdict[Point, int](lambda: 0)

  for line in lines:
    if _is_horizontal(line) or _is_vertical(line):
      for point in _iter_line(line):
        points[point] += 1

  return [
      point
      for point, strength in points.items()
      if strength >= minimum_strength
  ]


def _is_horizontal(line: Line) -> bool:
  return line.origin[1] == line.destination[1]


def _is_vertical(line: Line) -> bool:
  return line.origin[0] == line.destination[0]


def _iter_line(line: Line) -> Iterator[Point]:
  x_min = min(line.origin[0], line.destination[0])
  x_max = max(line.origin[0], line.destination[0])
  y_min = min(line.origin[1], line.destination[1])
  y_max = max(line.origin[1], line.destination[1])
  return itertools.product(range(x_min, x_max+1), range(y_min, y_max+1))


def parse_lines(lines: list[str]) -> list[Line]:
  return [_parse_line(line) for line in lines]


def _parse_line(line: str) -> Line:
  origin, destination = line.split(' -> ')
  return Line(
      _parse_point(origin),
      _parse_point(destination),
  )


def _parse_point(text: str) -> Point:
  x, y = text.split(',')
  return (int(x), int(y))
