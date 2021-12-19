import dataclasses
import re
from typing import Union


@dataclasses.dataclass(frozen=True)
class Number:
  left: Union['Number', int]
  right: Union['Number', int]

  def __add__(self, other) -> 'Number':
    return reduce(Number(self, other))

  def __repr__(self):
    return f'[{self.left},{self.right}]'


def parse_number(value: str) -> Number | int:
  if re.match(r'^\d+$', value):
    return int(value)

  left, right = _get_left_right(value)

  return Number(
      left=parse_number(left),
      right=parse_number(right),
  )


def _get_left_right(value: str) -> tuple[str, str]:
  if not value.startswith('[') or not value.endswith(']'):
    raise ValueError(f'{value} is not a stringified NumberPair')

  openings = 0
  index_right = 1
  while True:
    if value[index_right] == '[': openings += 1
    if value[index_right] == ']': openings -= 1
    index_right += 1

    if openings == 0:
      break
  while value[index_right] != ',':
    index_right += 1
  return value[1:index_right], value[index_right+1:-1]


def reduce(number: Number) -> Number:
  should_reduce = True
  while should_reduce:
    number, should_reduce = _reduce_once(number)
  return number


def _reduce_once(number: Number) -> tuple[Number, bool]:
  explode_result = explode(number)
  if explode_result.has_exploded:
    return explode_result.number, True

  split_result = split(number)
  if split_result.has_split:
    return split_result.number, True

  return number, False


@dataclasses.dataclass(frozen=True)
class ExplodeResult:
  number: Number
  has_exploded: bool = False
  to_add_left: int = 0
  to_add_right: int = 0


def explode(number: Number | int, depth=0) -> ExplodeResult:
  if isinstance(number, int):
    return ExplodeResult(number, has_exploded=False)

  if (
      depth >= 4
      and isinstance(number.left, int)
      and isinstance(number.right, int)
  ):
    return ExplodeResult(
        number=0,
        has_exploded=True,
        to_add_left=number.left,
        to_add_right=number.right,
    )

  result = explode(number.left, depth+1)
  if result.has_exploded:
    return ExplodeResult(
        number=Number(
            left=result.number,
            right=_add_to_left(number.right, result.to_add_right)
        ),
        has_exploded=True,
        to_add_left=result.to_add_left
    )

  result = explode(number.right, depth+1)
  if result.has_exploded:
    return ExplodeResult(
        number=Number(
            left=_add_to_right(number.left, result.to_add_left),
            right=result.number
        ),
        has_exploded=True,
        to_add_right=result.to_add_right
    )

  return ExplodeResult(number, has_exploded=False)


def _add_to_left(number: Number | int, to_add: int) -> Number | int:
  if to_add == 0:
    return number
  if isinstance(number, int):
    return number + to_add
  return Number(
      left=_add_to_left(number.left, to_add),
      right=number.right,
  )


def _add_to_right(number: Number | int, to_add: int) -> Number | int:
  if to_add == 0:
    return number
  if isinstance(number, int):
    return number + to_add
  return Number(
      left=number.left,
      right=_add_to_right(number.right, to_add),
  )


@dataclasses.dataclass(frozen=True)
class SplitResult:
  number: Number
  has_split: bool = False


def split(number: Number | int) -> SplitResult:
  if isinstance(number, int):
    if number >= 10:
      half = number // 2
      return SplitResult(Number(half, number - half), True)
    return SplitResult(number, False)

  split_left = split(number.left)
  if split_left.has_split:
    return SplitResult(Number(split_left.number, number.right), True)

  split_right = split(number.right)
  if split_right.has_split:
    return SplitResult(Number(number.left, split_right.number), True)

  return SplitResult(number, False)


def get_magnitude(number: Number | int) -> int:
  if isinstance(number, int):
    return number

  return 3*get_magnitude(number.left) + 2*get_magnitude(number.right)
