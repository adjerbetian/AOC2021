from typing import Callable
import day03.binary as binary


Binary = binary.Binary


class Report(tuple[Binary]):
  @property
  def size(self):
    return len(self)

  @property
  def n_bits(self):
    return len(self[0])


def build_report(lines: list[str]) -> Report:
  return Report(
      binary.parse(line)
      for line in lines
  )


def get_power_consumption(report: Report):
  return get_gamma_rate(report) * get_epsilon(report)


def get_gamma_rate(report: Report) -> int:
  half = report.size // 2
  binary_result = Binary(
      sum(b[bit] for b in report) > half
      for bit in range(report.n_bits)
  )
  return binary.to_int(binary_result)


def get_epsilon(report: Report) -> int:
  return 2 ** report.n_bits - 1 - get_gamma_rate(report)


def get_life_support_rating(report: Report) -> int:
  return get_co2_scrubber_rating(report) * get_oxygen_generator_rating(report)


def get_oxygen_generator_rating(report: Report) -> int:
  binary_result = _dichotomize(
      report,
      split_predicate=lambda value, j: value[j],
      keep_predicate=lambda v0, v1: v1 if len(v1) >= len(v0) else v0,
  )
  return binary.to_int(binary_result)


def get_co2_scrubber_rating(report) -> int:
  binary_result = _dichotomize(
      report,
      split_predicate=lambda value, j: value[j],
      keep_predicate=lambda v0, v1: v1 if len(v1) < len(v0) else v0,
  )
  return binary.to_int(binary_result)


def _dichotomize(
    report: Report,
    split_predicate: Callable[[Binary, int], bool],
    keep_predicate: Callable[[list[Binary], list[Binary]], list[Binary]],
) -> Binary:
  binaries = report
  for j in range(report.n_bits):
    left, right = _split_binaries(binaries, lambda b: split_predicate(b, j))
    binaries = keep_predicate(left, right)
    if len(binaries) == 1:
      return binaries[0]
  raise ValueError(f'Did not reach unique value in: {binaries}')


def _split_binaries(
    binaries: list[Binary],
    predicate: Callable[[Binary], bool],
):
  left: list[Binary] = []
  right: list[Binary] = []
  for b in binaries:
    if predicate(b):
      right.append(b)
    else:
      left.append(b)
  return left, right
