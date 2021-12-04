import utils
import day03.diagnostic_report as diagnostic_report


def main():
  lines = utils.read_lines('input.txt')
  report = diagnostic_report.build_report(lines)

  log('part 1', diagnostic_report.get_power_consumption(report))
  log('part 2', diagnostic_report.get_life_support_rating(report))


def log(*args):
  print('Day 03:', *args)


if __name__ == '__main__':
  main()
