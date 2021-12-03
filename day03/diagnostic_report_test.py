import unittest

import day03.diagnostic_report as diagnostic_report


report = diagnostic_report.build_report([
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
])


class TestDay3(unittest.TestCase):

  def test_power_consumption(self):
    self.assertEqual(198, diagnostic_report.get_power_consumption(report))

  def test_diagnostic_report_gamma_rate(self):
    self.assertEqual(22, diagnostic_report.get_gamma_rate(report))

  def test_diagnostic_report_epsilon(self):
    self.assertEqual(9, diagnostic_report.get_epsilon(report))

  def test_life_support_rating(self):
    self.assertEqual(230, diagnostic_report.get_life_support_rating(report))

  def test_oxygen_generator_rating(self):
    self.assertEqual(23, diagnostic_report.get_oxygen_generator_rating(report))

  def test_co2_scrubber_rating(self):
    self.assertEqual(10, diagnostic_report.get_co2_scrubber_rating(report))


if __name__ == '__main__':
  unittest.main()
