reports = []
total_safe = 0

with open('input.txt', 'r') as file:
  for line in file.readlines():
    # Turn each report into an array of integers
    data_points = [int(i) for i in line.split()]
    reports.append(data_points)

def is_report_safe(report) -> bool:

  is_increasing = None

  for i in range(len(report)-1):

    # Is the next element in the report higher than the current?
    increase = report[i] < report[i+1]

    # Oh no! We were going one direction, but now we're going the other!
    if is_increasing is not None and is_increasing != increase:
      return False
    
    if is_increasing is None:
      is_increasing = increase

    change = abs(report[i] - report[i+1])

    # Oh no! The change is too low or too high!
    if change not in [1, 2, 3]:
      return False
    
  # Nothing about this report is unsafe :)
  return True

for report in reports:
  if is_report_safe(report):
    total_safe += 1

print(total_safe)