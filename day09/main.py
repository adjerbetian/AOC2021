from typing import Iterable

import utils

import day09.heightmap as heightmap


def main():
  input_map = heightmap.Heightmap([
      [int(h) for h in line]
      for line in utils.read_lines('input.txt')
  ])
  log('part 1:', input_map.get_risk_level())

  basins = input_map.get_basins()
  basin_sizes = sorted(map(len, basins))
  log('part 2:', multiply(basin_sizes[-3:]))


def log(*args):
  print('Day 09:', *args)


def multiply(items: Iterable[int]) -> int:
  result = 1
  for x in items:
    result *= x
  return result


if __name__ == '__main__':
  main()
