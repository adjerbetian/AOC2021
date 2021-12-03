Binary = list[bool]


class DiagnosticReport:
  def __init__(self, binary_numbers: list[str]):
    self.report: list[Binary] = [
        [bit == '1' for bit in line]
        for line in binary_numbers
    ]

  def get_power_consumption(self):
    return self.get_gamma_rate() * self.get_epsilon()

  def get_gamma_rate(self) -> int:
    n = len(self.report)
    m = len(self.report[0])

    return binary_to_int([
        sum(self.report[i][j] for i in range(n)) > n / 2
        for j in range(m)
    ])

  def get_epsilon(self) -> int:
    m = len(self.report[0])
    return 2**m - 1 - self.get_gamma_rate()


def binary_to_int(binary: Binary):
  value = 0
  power = 1
  for bit in reversed(binary):
    value += power * bit
    power *= 2
  return value
