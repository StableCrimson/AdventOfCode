from pathlib import Path

script_dir = Path(__file__).parent

def contains_pattern(value: int) -> bool:

  str_value = str(value)

  if len(str_value) % 2 == 1: # Must have even length, as patter nmust fit twice
    return False

  pattern = str_value[:len(str_value) // 2]
  return pattern * 2 == str_value

with open(script_dir / 'input.txt') as f:
  ranges = f.read().split(',')

split_ranges = []

for r in ranges:
  start, end = r.split('-')
  split_ranges.append((int(start), int(end)))

sum_invalid = 0

for start, end in split_ranges:

  values = { i for i in range(start, end + 1) }

  for value in values:
    if contains_pattern(value):
      sum_invalid += value

print(sum_invalid)