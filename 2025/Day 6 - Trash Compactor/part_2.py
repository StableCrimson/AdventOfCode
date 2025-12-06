from pathlib import Path
from typing import List

script_dir = Path(__file__).parent

def digest_problem_top_down(problem: List[str]) -> List[str]:
  operator = problem[-1].strip()

  new_digits = []

  for number in problem[:-1]:
    for i, c in enumerate(number):
      if len(new_digits) > i:
        new_digits[i] += c
      else:
        new_digits.append(c)

  return [*[digit.strip() for digit in new_digits], operator]


with open(script_dir / 'input.txt') as f:
  raw_data = f.readlines()

  operator_line = raw_data[-1]
  operator_indices = []

  raw_problems = []

  for i, c in enumerate(operator_line):
    if not c.isspace():
      operator_indices.append(i)

  for i in range(len(operator_indices)):
    start = operator_indices[i]

    if i + 1 < len(operator_indices):
      end = operator_indices[i+1] - 1 # There's an extra space between problems
      raw_problems.append([line[start:end] for line in raw_data])
    else:
      raw_problems.append([line[start:-1] for line in raw_data])

  problems = [digest_problem_top_down(problem) for problem in raw_problems]


def solve(problem: List[str]) -> int:
  operator = problem[-1]
  total = int(problem[0])

  for i in range(1, len(problem[:-1])):
    if operator == '+':
      total += int(problem[i])
    else:
      total *= int(problem[i])
      
  return total

total = sum(solve(problem) for problem in problems)
print(total)