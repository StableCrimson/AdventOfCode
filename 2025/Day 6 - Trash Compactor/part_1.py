from pathlib import Path
from typing import List

script_dir = Path(__file__).parent

with open(script_dir / 'input.txt') as f:
  raw_data = [line.strip().split() for line in f.readlines()]
  problems = []

  for i in range(len(raw_data[0])):
    problems.append([line[i] for line in raw_data])


def solve(problem: List[str]) -> int:
  operator = problem[-1]
  total = int(problem[0])

  for i in range(1, len(problem[:-1])):
    if operator == '+':
      total += int(problem[i])
    else:
      total *= int(problem[i])
      
  return total

total = 0

for problem in problems:
  total += solve(problem)

print(total)