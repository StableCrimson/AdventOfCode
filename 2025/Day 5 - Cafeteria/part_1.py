with open('input.txt') as f:
  lines = [line.strip() for line in f.readlines()]

  recorded_all_ranges = False

  ranges = []
  records = []

  for line in lines:
    if line == '':
      recorded_all_ranges = True
      continue

    if not recorded_all_ranges:
      start, end = line.split('-')
      ranges.append((int(start), int(end)))
    else:
      records.append(int(line))

  print(ranges, records)

total_safe = 0

for record in records:
  if any(start <= record <= end for start, end in ranges):
    print(f'record {record} is safe')
    total_safe += 1

print(total_safe)

