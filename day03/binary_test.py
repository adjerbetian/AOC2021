import unittest

import day03.binary as binary


class TestBinary(unittest.TestCase):

  def test_parse_binary(self):
    self.assertEqual([True, False, True], binary.parse('101'))

  def test_binary_to_int(self):
    self.assertEqual(1, binary.to_int(binary.Binary([True])))
    self.assertEqual(2, binary.to_int(binary.Binary([True, False])))
    self.assertEqual(5, binary.to_int(binary.Binary([True, False, True])))

  def test_binary_to_string(self):
    self.assertEqual('101', f'{binary.Binary([True, False, True])}')


if __name__ == '__main__':
  unittest.main()
