def find_optimal_position(positions: list[int]) -> tuple[int, int]:
  best_position = positions[0]
  best_score = get_position_score(positions, best_position)
  for position in range(min(positions), max(positions)):
    score = get_position_score(positions, position)
    if score < best_score:
      best_score = score
      best_position = position
  return best_position, best_score


def get_position_score(positions: list[int], position: int) -> int:
  return sum(_get_fuel(p, position) for p in positions)


def _get_fuel(p1: int, p2: int) -> int:
  d = abs(p2 - p1)
  return d * (d + 1) // 2
