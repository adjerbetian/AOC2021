from day02 import parse_instructions
from day02 import Submarine


def main():
  lines = read_lines('input.txt')
  instructions = parse_instructions(lines)
  submarine = Submarine()

  submarine.follow_instructions(instructions)

  log(submarine.x * submarine.depth)


def read_lines(file_path: str) -> list[str]:
  with open(file_path, 'r') as file:
    return file.read().splitlines()


def log(*args):
  print(f'Day 02:', *args)


if __name__ == '__main__':
  main()
