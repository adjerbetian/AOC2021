import day05.vents as vents
import utils


def main():
  lines = vents.parse_lines(utils.read_lines('input.txt'))

  log('part 1', len(vents.get_points_with_strength_at_least(lines, 2)))


def log(*args):
  print('Day 05:', *args)


if __name__ == '__main__':
  main()
