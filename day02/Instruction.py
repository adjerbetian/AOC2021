import abc

from day02.State import State


class Instruction(metaclass=abc.ABCMeta):
  def __init__(self, units: int):
    self.units = units

  @abc.abstractmethod
  def update_state(self, state: State) -> State:
    raise NotImplementedError()


class Forward(Instruction):
  def update_state(self, state: State) -> State:
    return State(
        x=state.x + self.units,
        depth=state.depth + state.aim * self.units,
        aim=state.aim
    )


class Up(Instruction):
  def update_state(self, state: State) -> State:
    return State(
        x=state.x,
        depth=state.depth,
        aim=state.aim - self.units,
    )


class Down(Instruction):
  def update_state(self, state: State) -> State:
    return State(
        x=state.x,
        depth=state.depth,
        aim=state.aim + self.units,
    )


def parse_instructions(lines: list[str]) -> list[Instruction]:
  return [parse_instruction(line) for line in lines]


def parse_instruction(line: str) -> Instruction:
  direction, units = line.split()
  units = int(units)
  match direction:
    case 'forward': return Forward(units)
    case 'up': return Up(units)
    case 'down': return Down(units)
    case _: raise ValueError(f'Wrong instruction "{line}"')
