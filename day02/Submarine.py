from day02.Instruction import Instruction
from day02.Localisation import Localisation


class Submarine:
  def __init__(self):
    self.localisation = Localisation(0, 0)

  @property
  def x(self):
    return self.localisation.x

  @property
  def depth(self):
    return self.localisation.depth

  def follow_instructions(self, instructions: list[Instruction]):
    for instruction in instructions:
      self.localisation = instruction.move(self.localisation)
