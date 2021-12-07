import utils

import day07.crabs1 as crabs1
import day07.crabs2 as crabs2


def main():
  positions = utils.read_int_line('input.txt')

  best_position, best_score = crabs1.find_optimal_position(positions)
  log('part 1:', best_score)

  best_position, best_score = crabs2.find_optimal_position(positions)
  log('part 2:', best_score)


def log(*args):
  print('Day 07:', *args)


if __name__ == '__main__':
  main()
