class Binary(list[bool]):
  def __str__(self):
    return ''.join(
        '1' if bit else '0'
        for bit in self
    )


def to_int(binary: Binary):
  value = 0
  power = 1
  for bit in reversed(binary):
    value += power * bit
    power *= 2
  return value


def parse(line: str) -> Binary:
  return Binary(bit == '1' for bit in line)
