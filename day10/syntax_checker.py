PAIRS = [
    '()',
    '[]',
    '<>',
    '{}',
]

SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    None: 0
}


def get_first_wrong_character(navigation: str) -> str | None:
  openings = []
  for char in navigation:
    if _is_opening(char):
      openings.append(char)
    else:
      if _does_closing_match_opening(char, openings[-1]):
        openings.pop()
      else:
        return char
  return None


def _is_opening(char: str) -> bool:
  return char in [pair[0] for pair in PAIRS]


def _does_closing_match_opening(closing: str, opening: str) -> bool:
  return opening + closing in PAIRS


def get_score(navigations: list[str]) -> int:
  return sum(
      SCORES[get_first_wrong_character(nav)]
      for nav in navigations
  )
