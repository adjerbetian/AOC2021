import unittest

import day10.syntax_checker as syntax_checker


class Day10Test(unittest.TestCase):

  def test_get_first_wrong_character(self):
    tests = [
        ('{([(<{}[<>[]}>{[]{[(<()>', '}'),
        ('[[<[([]))<([[{}[[()]]]', ')'),
        ('[{[{({}]{}}([{[{{{}}([]', ']'),
        ('[<(<(<(<{}))><([]([]()', ')'),
        ('<{([([[(<>()){}]>(<<{{', '>'),
    ]

    for nav, char in tests:
      with self.subTest(f'{nav} - {char}'):
        self.assertEqual(char, syntax_checker.get_first_wrong_character(nav))

  def test_get_missing_closings(self):
    tests = [
        ('[({(<(())[]>[[{[]{<()<>>', '}}]])})]'),
        ('[(()[<>])]({[<{<<[]>>(', ')}>]})'),
        ('(((({<>}<{<{<>}{[]{[]{}', '}}>}>))))'),
        ('{<[[]]>}<{[{[{[]{()[[[]', ']]}}]}]}>'),
        ('<{([{{}}[<[[[<>{}]]]>[]]', '])}>'),
    ]

    for nav, missing in tests:
      with self.subTest(f'{nav} - {missing}'):
        self.assertEqual(missing, syntax_checker.get_missing_closings(nav))

  def test_get_score1(self):
    score = syntax_checker.get_navigations_score1([
        '[({(<(())[]>[[{[]{<()<>>',
        '[(()[<>])]({[<{<<[]>>(',
        '{([(<{}[<>[]}>{[]{[(<()>',
        '(((({<>}<{<{<>}{[]{[]{}',
        '[[<[([]))<([[{}[[()]]]',
        '[{[{({}]{}}([{[{{{}}([]',
        '{<[[]]>}<{[{[{[]{()[[[]',
        '[<(<(<(<{}))><([]([]()',
        '<{([([[(<>()){}]>(<<{{',
        '<{([{{}}[<[[[<>{}]]]>[]]',
    ])

    self.assertEqual(26397, score)

  def test_get_score2(self):
    score = syntax_checker.get_navigations_score2([
        '[({(<(())[]>[[{[]{<()<>>',
        '[(()[<>])]({[<{<<[]>>(',
        '{([(<{}[<>[]}>{[]{[(<()>',
        '(((({<>}<{<{<>}{[]{[]{}',
        '[[<[([]))<([[{}[[()]]]',
        '[{[{({}]{}}([{[{{{}}([]',
        '{<[[]]>}<{[{[{[]{()[[[]',
        '[<(<(<(<{}))><([]([]()',
        '<{([([[(<>()){}]>(<<{{',
        '<{([{{}}[<[[[<>{}]]]>[]]',
    ])

    self.assertEqual(288957, score)
