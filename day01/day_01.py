
def main():
  depths = read_ints('input.txt')
  log(1, count_increases(depths))
  log(2, count_increases(depths, window_size=3))


def read_ints(file_path: str) -> list[int]:
  with open(file_path, 'r') as file:
    return [
        int(line)
        for line in file.read().splitlines()
    ]


def count_increases(
    depths: list[int],
    window_size=1,
) -> int:
  increases = 0
  for i in range(len(depths) - window_size):
    if depths[i + window_size] > depths[i]:
      increases += 1
  return increases


def log(part: int, *args):
  print(f'Day 01 - part {str(part)}:', *args)


if __name__ == '__main__':
  main()
