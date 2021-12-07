def read_int_line(param) -> list[int]:
  line = read_lines(param)[0]
  return [int(x) for x in line.split(',')]


def read_ints(file_path: str) -> list[int]:
  with open(file_path, 'r') as file:
    return [
        int(line)
        for line in file.read().splitlines()
    ]


def read_lines(file_path: str) -> list[str]:
  with open(file_path, 'r') as file:
    return file.read().splitlines()


def read_blocks(file_path: str) -> list[str]:
  with open(file_path, 'r') as file:
    return file.read().strip().split('\n\n')
