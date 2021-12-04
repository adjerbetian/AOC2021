import utils
from day02 import parse_instructions
from day02 import Submarine


def main():
  lines = utils.read_lines('input.txt')
  instructions = parse_instructions(lines)
  submarine = Submarine()

  submarine.follow_instructions(instructions)

  log(submarine.x * submarine.depth)


def log(*args):
  print(f'Day 02:', *args)


if __name__ == '__main__':
  main()
