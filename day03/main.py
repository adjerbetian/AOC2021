from day03.DiagnosticReport import DiagnosticReport


def main():
  lines = read_lines('input.txt')
  report = DiagnosticReport(lines)

  log('part 1', report.get_power_consumption())


def read_lines(file_path: str) -> list[str]:
  with open(file_path, 'r') as file:
    return file.read().splitlines()


def log(*args):
  print('Day 03:', *args)


if __name__ == '__main__':
  main()
