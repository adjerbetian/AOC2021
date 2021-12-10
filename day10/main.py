import utils

import day10.syntax_checker as syntax_checker


def main():
  navigations = utils.read_lines('input.txt')
  log('part 1:', syntax_checker.get_navigations_score1(navigations))
  log('part 2:', syntax_checker.get_navigations_score2(navigations))


def log(*args):
  print('Day 10:', *args)


if __name__ == '__main__':
  main()
