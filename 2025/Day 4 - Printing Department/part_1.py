from copy import deepcopy

with open('input.txt') as f:
  data = [[c for c in line.strip()] for line in f.readlines()]

visual = deepcopy(data)

width = len(data[0])
height = len(data)

def is_cell_occupied(x: int, y: int) -> bool:
  if x < 0 or x >= width:
    return False
  
  if y < 0 or y >= height:
    return False
  
  return data[y][x] == '@'


def is_roll_accessible(x: int, y: int, neighbor_cutoff: int, show_work: bool = False) -> bool:
  
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

  is_accessible = neighbors < neighbor_cutoff

  if is_accessible and show_work:
    visual[y][x] = 'x'

    for row in visual:
      print(''.join(row))
    print(f'Cell ({x},{y}) is acessible with {neighbors} neighbor(s)\n')

  return is_accessible


total_accessible = 0

for x in range(width):
  for y in range(height):
    if data[y][x] == '@' and is_roll_accessible(x, y, 4, False):
      total_accessible += 1

print(total_accessible)