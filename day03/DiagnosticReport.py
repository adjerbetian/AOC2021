from typing import Callable


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

  def get_life_support_rating(self) -> int:
    return self.get_co2_scrubber_rating() * self.get_oxygen_generator_rating()

  def get_oxygen_generator_rating(self) -> int:
    return self.dichotomize(
        split_predicate=lambda value, j: value[j],
        keep_predicate=lambda v0, v1: v1 if len(v1) >= len(v0) else v0,
    )

  def get_co2_scrubber_rating(self) -> int:
    return self.dichotomize(
        split_predicate=lambda value, j: value[j],
        keep_predicate=lambda v0, v1: v1 if len(v1) < len(v0) else v0,
    )

  def dichotomize(
      self,
      split_predicate: Callable[[Binary, int], bool],
      keep_predicate: Callable[[list[Binary], list[Binary]], list[Binary]],
  ) -> int:
    m = len(self.report[0])
    values = self.report
    for j in range(m):
      values0, values1 = _split_values(values, lambda v: split_predicate(v, j))
      values = keep_predicate(values0, values1)
      if len(values) == 1:
        return binary_to_int(values[0])
    raise ValueError(f'Did not reach unique value: {values}')


def _split_values(
    values: list[Binary],
    predicate: Callable[[Binary], bool]
):
  values0: list[Binary] = []
  values1: list[Binary] = []
  for value in values:
    if predicate(value):
      values1.append(value)
    else:
      values0.append(value)
  return values0, values1


def binary_to_int(binary: Binary):
  value = 0
  power = 1
  for bit in reversed(binary):
    value += power * bit
    power *= 2
  return value
