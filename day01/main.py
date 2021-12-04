import utils


def main():
  depths = utils.read_ints('input.txt')
  log(1, count_increases(depths))
  log(2, count_increases(depths, window_size=3))


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
