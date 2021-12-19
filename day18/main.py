import utils
import day18.snailfish as snailfish


def main():
  lines = utils.read_lines('input.txt')
  numbers = [snailfish.parse_number(line) for line in lines]
  result = numbers[0]
  for i in range(1, len(numbers)):
    result = result + numbers[i]
  log('part 1', snailfish.get_magnitude(result))

  result = 0
  for i in range(len(lines)):
    for j in range(len(lines)):
      if i == j:
        continue
      result = max(result, snailfish.get_magnitude(numbers[i] + numbers[j]))
  log('part 2', result)


def log(*args):
  print('Day 18:', *args)


if __name__ == '__main__':
  main()
