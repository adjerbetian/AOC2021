import dataclasses
from collections import defaultdict
from typing import Iterable


@dataclasses.dataclass(frozen=True)
class Point:
  x: int
  y: int

  def __str__(self):
    return f'{self.x},{self.y}'


@dataclasses.dataclass(frozen=True)
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
    for point in _iter_line(line):
      points[point] += 1

  return [
      point
      for point, strength in points.items()
      if strength >= minimum_strength
  ]


def _iter_line(line: Line) -> Iterable[Point]:
  dx = line.destination.x - line.origin.x
  dy = line.destination.y - line.origin.y
  n = max(abs(dx), abs(dy))
  dx = int(dx / n)
  dy = int(dy / n)

  for i in range(n + 1):
    yield (line.origin.x + i * dx, line.origin.y + i * dy)


def print_map(vents_map: dict[Point]):
  x_max, y_max = 0, 0
  for point in vents_map.keys():
    x_max = max(x_max, point.x)
    y_max = max(y_max, point.y)

  for y in range(y_max + 1):
    print(''.join([
        str(vents_map[Point(x, y)]) if vents_map[Point(x, y)] > 0 else '.'
        for x in range(x_max + 1)
    ]))


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
  return Point(int(x), int(y))
