from typing import List
from pathlib import Path

script_dir = Path(__file__).parent

with open(script_dir / 'input.txt') as f:
  data = [[c for c in line.strip()] for line in f.readlines()]

width = len(data[0])
height = len(data)

def is_cell_occupied(x: int, y: int) -> bool:
  if x < 0 or x >= width:
    return False
  
  if y < 0 or y >= height:
    return False
  
  return data[y][x] == '@'


def is_roll_accessible(x: int, y: int, neighor_cutoff: int) -> bool:
  
  neighbors = 0

  # Row Above
  if is_cell_occupied(x - 1, y - 1):
    neighbors += 1

  if is_cell_occupied(x    , y - 1):
    neighbors += 1

  if is_cell_occupied(x + 1, y - 1):
    neighbors += 1

  # Same Row
  if is_cell_occupied(x - 1, y):
    neighbors += 1

  if is_cell_occupied(x + 1, y):
    neighbors += 1

  # Row Below
  if is_cell_occupied(x - 1, y + 1):
    neighbors += 1

  if is_cell_occupied(x    , y + 1):
    neighbors += 1

  if is_cell_occupied(x + 1, y + 1):
    neighbors += 1

  return neighbors < neighor_cutoff

def do_removal_pass(data: List[List[str]], show_work: bool = False) -> int:

  to_be_removed = []

  for x in range(width):
    for y in range(height):
      if data[y][x] == '@' and is_roll_accessible(x, y, 4):
        to_be_removed.append((x, y))


  if show_work:
    
    for x, y in to_be_removed:
      data[y][x] = 'X'
    
    for row in data:
      print(''.join(row))

    print(f'Removed {len(to_be_removed)} rolls\n')

  for x, y in to_be_removed:
    data[y][x] = '.'

  return len(to_be_removed)

total_removed = 0
last_pass_removed = -1

while last_pass_removed != 0:
  removed = do_removal_pass(data, True)
  total_removed += removed
  last_pass_removed = removed

print(total_removed)
