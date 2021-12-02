import dataclasses


@dataclasses.dataclass
class State:
  x: int = 0
  depth: int = 0
  aim: int = 0
