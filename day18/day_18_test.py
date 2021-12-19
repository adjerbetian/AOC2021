import unittest

import day18.snailfish as snailfish


class Day18Test(unittest.TestCase):

  def test_parse(self):
    for number in [
        '[0,13]',
        '[15,[0,13]]',
        '[[4,[15,[0,13]]],1]',
        '[[[[0,7],4],[15,[0,13]]],[1,1]]',
    ]:
      with self.subTest(number):
        self.assertEqual(number, repr(snailfish.parse_number(number)))

  def test_simple_add(self):
    left = snailfish.parse_number('[1,2]')
    right = snailfish.parse_number('[[3,4],5]')

    self.assertEqual(left + right, snailfish.parse_number('[[1,2],[[3,4],5]]'))

  def test_explode_1(self):
    number = snailfish.parse_number('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')

    result = snailfish.explode(number)

    self.assertTrue(result.has_exploded)
    self.assertEqual(
        result.number,
        snailfish.parse_number('[[[[0,7],4],[7,[[8,4],9]]],[1,1]]'))

  def test_explode_2(self):
    number = snailfish.parse_number('[[[[0,7],4],[7,[[8,4],9]]],[1,1]]')

    result = snailfish.explode(number)

    self.assertTrue(result.has_exploded)
    self.assertEqual(
        result.number,
        snailfish.parse_number('[[[[0,7],4],[15,[0,13]]],[1,1]]'))

  def test_explode_3(self):
    number = snailfish.parse_number('[[[[0,7],4],[15,[0,13]]],[1,1]]')

    result = snailfish.explode(number)

    self.assertFalse(result.has_exploded)
    self.assertEqual(result.number, number)

  def test_split_no_split(self):
    number = snailfish.parse_number('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')

    result = snailfish.split(number)

    self.assertFalse(result.has_split)
    self.assertEqual(result.number, number)

  def test_split_with_split(self):
    number = snailfish.parse_number('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]')

    result = snailfish.split(number)

    self.assertTrue(result.has_split)
    self.assertEqual(
        '[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]',
        repr(result.number))

  def test_add_with_reduce(self):
    left = snailfish.parse_number('[[[[4,3],4],4],[7,[[8,4],9]]]')
    right = snailfish.parse_number('[1,1]')

    self.assertEqual(
        left + right,
        snailfish.parse_number('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'))

  def test_magnitude(self):
    for number, magnitude in [
        ('[9,1]', 3*9 + 2*1),
        ('[[1,2],[[3,4],5]]', 143),
        ('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]', 1384),
        ('[[[[1,1],[2,2]],[3,3]],[4,4]]', 445),
        ('[[[[3,0],[5,3]],[4,4]],[5,5]]', 791),
        ('[[[[5,0],[7,4]],[5,5]],[6,6]]', 1137),
        ('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]', 3488),
    ]:
      with self.subTest(number):
        self.assertEqual(
            magnitude,
            snailfish.get_magnitude(snailfish.parse_number(number)),
        )
