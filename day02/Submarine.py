from day02.Instruction import Instruction
from day02.State import State


class Submarine:
  def __init__(self):
    self.state = State()

  @property
  def x(self):
    return self.state.x

  @property
  def depth(self):
    return self.state.depth

  def follow_instructions(self, instructions: list[Instruction]):
    for instruction in instructions:
      self.state = instruction.update_state(self.state)
