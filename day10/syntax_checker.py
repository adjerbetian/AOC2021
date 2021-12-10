PAIRS = [
    '()',
    '[]',
    '<>',
    '{}',
]


def get_navigations_score1(navigations: list[str]) -> int:
  scores = {
      ')': 3,
      ']': 57,
      '}': 1197,
      '>': 25137,
      None: 0
  }

  return sum(
      scores[get_first_wrong_character(nav)]
      for nav in navigations
  )


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


def get_navigations_score2(navigations: list[str]) -> int:
  scores = sorted([
      get_navigation_score2(nav)
      for nav in navigations
      if not is_corrupted(nav)
  ])
  return scores[len(scores) // 2]


def get_navigation_score2(navigation: str) -> int:
  scores = {
      ')': 1,
      ']': 2,
      '}': 3,
      '>': 4,
  }
  score = 0
  missing_closings = get_missing_closings(navigation)
  for char in missing_closings:
    score = 5 * score + scores[char]
  return score


def get_missing_closings(navigation: str) -> str:
  openings = []
  for char in navigation:
    if _is_opening(char):
      openings.append(char)
    else:
      if _does_closing_match_opening(char, openings[-1]):
        openings.pop()
      else:
        raise ValueError(f'The navigation "{navigation}" is corrupted.')
  openings.reverse()
  return ''.join([_get_closing(opening) for opening in openings])


def is_corrupted(navigation: str) -> bool:
  return get_first_wrong_character(navigation) is not None


def _is_opening(char: str) -> bool:
  return char in [pair[0] for pair in PAIRS]


def _does_closing_match_opening(closing: str, opening: str) -> bool:
  return opening + closing in PAIRS


def _get_closing(opening: str) -> str:
  for pair in PAIRS:
    if opening == pair[0]:
      return pair[1]
  raise ValueError(f'Opening "{opening}" not found.')
