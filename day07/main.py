import utils

import day07.crabs as crabs


def main():
  positions = utils.read_int_line('input.txt')

  best_position, best_score = crabs.find_optimal_position(positions)
  log('part 1:', best_score)


def log(*args):
  print('Day 07:', *args)


if __name__ == '__main__':
  main()
