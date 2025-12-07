from pathlib import Path
from typing import List, Tuple
from functools import cache

script_dir = Path(__file__).parent

with open(script_dir / 'input.txt') as f:
  grid = [[c for c in line.strip()] for line in f.readlines()]

@cache
def num_unique_paths(x: int, y: int) -> int:

  width = len(grid[0])
  height = len(grid)

  # Coordinate is not a valid path
  if x < 0 or x >= width or y < 0 or y >= height:
    return 0

  # This path has left the grid
  if y + 1 == height:
    return 1

  # Calculate the left and right subtrees of this splitter
  if grid[y+1][x] == '^':
    return num_unique_paths(x-1, y+1) + num_unique_paths(x+1, y+1)
  
  # Not invalid, still in the grid, and not a splitter, just propogate
  return num_unique_paths(x, y+1)


def get_emitter_position(grid: List[List[str]]) -> Tuple[int, int]:
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == 'S':
        return x, y
      
  raise RuntimeError('Emitter was not found in the grid!')


print(num_unique_paths(*get_emitter_position(grid)))
