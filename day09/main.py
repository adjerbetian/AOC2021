import utils

import day09.heightmap as heightmap


def main():
  input_map = heightmap.Heightmap([
      [int(h) for h in line]
      for line in utils.read_lines('input.txt')
  ])
  log('part 1:', input_map.get_risk_level())


def log(*args):
  print('Day 09:', *args)


if __name__ == '__main__':
  main()
