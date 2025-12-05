from typing import Tuple, List

with open('input.txt') as f:
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

def collapse_all_ranges(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:

  done = False
  new_ranges = ranges.copy()

  # `done` is set if we can iterate all of the ranges and detect no overlaps
  while not done:

    removed_index = -1

    for i in range(len(new_ranges) - 1):

      if removed_index != -1:
        del new_ranges[removed_index]
        break

      for j in range(i+1, len(new_ranges)):
        if do_ranges_overlap(new_ranges[i], new_ranges[j]):
          collapsed = collapse_range(new_ranges[i], new_ranges[j])
          new_ranges[i] = collapsed
          removed_index = j
          break

    else:

      if removed_index != -1:
        del new_ranges[removed_index]
        break

      done = True
          
  return new_ranges

collapsed_ranges = collapse_all_ranges(ranges)
total_safe = 0

for start, end in collapsed_ranges:
  total_safe += (end - start) + 1
