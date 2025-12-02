def contains_pattern(value: int) -> bool:

  str_value = str(value)

  if len(str_value) == 1: # Can't have a pattern if only a digit
    return False

  for window_size in range(1, len(str_value) // 2 + 1):

    pattern = str_value[:window_size]
    repetitions = len(str_value) // window_size

    if pattern * repetitions == str_value:
      return True
    
  return False

with open('input.txt') as file:
  ranges = file.read().split(',')

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