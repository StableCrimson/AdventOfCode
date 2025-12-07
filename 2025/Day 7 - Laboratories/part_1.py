from pathlib import Path
from typing import List, Tuple

script_dir = Path(__file__).parent

def get_emitter_position(grid: List[List[str]]) -> Tuple[int, int]:
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == 'S':
        return x, y
      
  raise RuntimeError('Emitter was not found in the grid!')


with open(script_dir / 'input.txt') as f:
  grid = [[c for c in line.strip()] for line in f.readlines()]

x, y = get_emitter_position(grid)
print(grid)
print(x, y)

grid[y+1][x] = '|'

num_splits = 0

for i in range(2, len(grid)):
  for j, c in enumerate(grid[i]):
    if grid[i-1][j] == '|':
      if grid[i][j] == '^':
        num_splits += 1

        if j != 0:
          grid[i][j-1] = '|'

        if j < len(grid[0]) - 1:
          grid[i][j+1] = '|'

      else:
        grid[i][j] = '|'


for row in grid:
  print(''.join(row))

print(f'The beam was split {num_splits} times')





