import unittest

import day10.syntax_checker as syntax_checker


class Day07Test(unittest.TestCase):

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

  def test_get_score(self):
    score = syntax_checker.get_score([
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
