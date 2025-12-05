from pathlib import Path

script_dir = Path(__file__).parent

reports = []
total_safe = 0

with open(script_dir / 'input.txt') as f:
  for line in f.readlines():
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

def can_be_dampened(report: list) -> bool:
  subreports = []

  # Create a list of all possible dampened reports 
  for i in range(len(report)):
    subreports.append(report[:i] + report[i+1:])

  # Are any of the dampened reports safe?
  return any(is_report_safe(subreport) for subreport in subreports)


for report in reports:
  if is_report_safe(report):
    total_safe += 1

  # Uh oh! The report is unsafe! Let's try running the dampener
  elif can_be_dampened(report):
    total_safe += 1

print(total_safe)