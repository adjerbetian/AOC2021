import unittest

from day03.DiagnosticReport import DiagnosticReport
from day03.DiagnosticReport import binary_to_int

DIAGNOSTIC_REPORT = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]


class TestDay3(unittest.TestCase):

  def test_binary_to_int(self):
    self.assertEqual(1, binary_to_int([True]))
    self.assertEqual(2, binary_to_int([True, False]))
    self.assertEqual(9, binary_to_int([True, False, False, True]))

  def test_power_consumption(self):
    report = DiagnosticReport(DIAGNOSTIC_REPORT)

    self.assertEqual(198, report.get_power_consumption())

  def test_diagnostic_report_gamma_rate(self):
    report = DiagnosticReport(DIAGNOSTIC_REPORT)

    self.assertEqual(22, report.get_gamma_rate())

  def test_diagnostic_report_epsilon(self):
    report = DiagnosticReport(DIAGNOSTIC_REPORT)

    self.assertEqual(9, report.get_epsilon())


if __name__ == '__main__':
  unittest.main()
