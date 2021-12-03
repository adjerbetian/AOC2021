import day03.diagnostic_report as DiagnosticReport


def main():
  lines = read_lines('input.txt')
  report = DiagnosticReport.build_report(lines)

  log('part 1', DiagnosticReport.get_power_consumption(report))
  log('part 2', DiagnosticReport.get_life_support_rating(report))


def read_lines(file_path: str) -> list[str]:
  with open(file_path, 'r') as file:
    return file.read().splitlines()


def log(*args):
  print('Day 03:', *args)


if __name__ == '__main__':
  main()
