import utils

import day06.lanternfish as lanternfish


def main():
  ages = utils.read_int_line('input.txt')
  population0 = lanternfish.build_population(ages)

  population80 = lanternfish.pass_n_days(population0, 80)
  log('part 1:', lanternfish.get_population_count(population80))

  population256 = lanternfish.pass_n_days(population0, 256)
  log('part 2:', lanternfish.get_population_count(population256))


def log(*args):
  print('Day 06:', *args)


if __name__ == '__main__':
  main()
