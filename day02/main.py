from day02.Instruction import parse_instructions
from day02.Submarine import Submarine


def main():
  lines = read_lines('input.txt')
  instructions = parse_instructions(lines)
  submarine = Submarine()

  submarine.follow_instructions(instructions)

  log(1, submarine.x * submarine.depth)


def read_lines(file_path: str) -> list[str]:
  with open(file_path, 'r') as file:
    return file.read().splitlines()


def log(part: int, *args):
  print(f'Day 02 - part {str(part)}:', *args)


if __name__ == '__main__':
  main()
