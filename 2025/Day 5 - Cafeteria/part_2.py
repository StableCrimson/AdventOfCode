from pathlib import Path
from typing import Tuple, List

script_dir = Path(__file__).parent

with open(script_dir / 'input.txt') as f:
  lines = [line.strip() for line in f.readlines()]

  ranges = []

  for line in lines:
    if line == '':
      break

    start, end = line.split('-')
    ranges.append((int(start), int(end)))


def do_ranges_overlap(a: Tuple[int, int], b: Tuple[int, int]) -> bool:

  # B is a subset of A OR A and B overlap on one end
  if a[0] <= b[0] <= a[1]:
    return True

  if a[0] <= b[1] <= a[1]:
    return True

  # A is a subset of B
  if a[0] >= b[0] and a[1] <= b[1]:
    return True

  return False


def collapse_range(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
  return (min(a[0], b[0]), max(a[1], b[1]))


def collapse_all_ranges(ranges: List[Tuple[int, int]]):

  done = False

  # `done` is set if we can iterate all of the ranges and detect no overlaps
  while not done:

    removed_index = -1

    for i in range(len(ranges) - 1):

      if removed_index != -1:
        del ranges[removed_index]
        break

      for j in range(i + 1, len(ranges)):
        if do_ranges_overlap(ranges[i], ranges[j]):
          collapsed = collapse_range(ranges[i], ranges[j])
          ranges[i] = collapsed
          removed_index = j
          break

    else:

      if removed_index != -1:
        del ranges[removed_index]
        break

      done = True


collapse_all_ranges(ranges)
total_safe = 0

for start, end in ranges:
  total_safe += (end - start) + 1

print(total_safe)
