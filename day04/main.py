import re

import utils
from day04.board import Board
from day04.board import Grid
import day04.game as game


def main():
  [numbers_to_draw, *grids] = utils.read_blocks('input.txt')

  numbers_to_draw = parse_numbers(numbers_to_draw, ',')
  boards = [Board(parse_grid(grid)) for grid in grids]

  log('part 1:', game.get_first_winner_score(boards, numbers_to_draw))
  log('part 2:', game.get_last_winner_score(boards, numbers_to_draw))


def parse_numbers(numbers_to_draw: str, sep: str):
  return [int(v) for v in re.split(sep, numbers_to_draw)]


def parse_grid(lines: str) -> Grid:
  return [
      parse_numbers(line.strip(), r'\s+')
      for line in lines.split('\n')
  ]


def log(*args):
  print('Day 04:', *args)


if __name__ == '__main__':
  main()
