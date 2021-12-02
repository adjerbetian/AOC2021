import abc

from day02.Localisation import Localisation


class Instruction(metaclass=abc.ABCMeta):
  def __init__(self, units: int):
    self.units = units

  @abc.abstractmethod
  def move(self, localisation: Localisation) -> Localisation:
    raise NotImplementedError()


class Forward(Instruction):
  def move(self, localisation: Localisation) -> Localisation:
    return Localisation(
        localisation.x + self.units,
        localisation.depth,
    )


class Up(Instruction):
  def move(self, localisation: Localisation) -> Localisation:
    return Localisation(
        localisation.x,
        localisation.depth - self.units,
    )


class Down(Instruction):
  def move(self, localisation: Localisation) -> Localisation:
    return Localisation(
        localisation.x,
        localisation.depth + self.units,
    )


def parse_instructions(lines: list[str]) -> list[Instruction]:
  return [parse_instruction(line) for line in lines]


def parse_instruction(line: str) -> Instruction:
  direction, units = line.split()
  units = int(units)
  if direction == 'forward': return Forward(units)
  if direction == 'up': return Up(units)
  if direction == 'down': return Down(units)
  raise ValueError(f'Wrong instruction "{line}"')
