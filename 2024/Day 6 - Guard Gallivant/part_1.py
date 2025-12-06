from pathlib import Path
from typing import List, Tuple
from enum import Enum

script_dir = Path(__file__).parent

class Direction(Enum):
  Up = 0
  Down = 1
  Left = 2
  Right = 3

NEXT_DIRECTION: List[Direction] = [ Direction.Right, Direction.Left, Direction.Up, Direction.Down ]

class Guard:

  x: int
  y: int
  direction: Direction
  grid: List[List[str]]

  def __init__(self, grid: List[List[str]]):
    self.grid = grid
    self.x, self.y = self.find_in_grid()
    self.direction = Direction.Up

  def __str__(self) -> str:
    return f'X: {self.x:03}, Y: {self.y:03}, Direction: {self.direction.name}'

  def step(self):

    next_pos = self.next_position()
    self.grid[self.y][self.x] = 'X'

    if not self.in_bounds(*next_pos, len(grid[0]), len(grid)):
      raise RuntimeError('Guard has left the grid!')
    
    if grid[next_pos[1]][next_pos[0]] == '#':
      self.direction = NEXT_DIRECTION[self.direction.value]
      self.step()
      return
    
    self.x = next_pos[0]
    self.y = next_pos[1]


  def next_position(self) -> Tuple[int, int]:
    if self.direction == Direction.Up:
      return (self.x, self.y - 1)
    if self.direction == Direction.Down:
      return (self.x, self.y + 1)
    if self.direction == Direction.Left:
      return (self.x - 1, self.y)
    if self.direction == Direction.Right:
      return (self.x + 1, self.y)
    
    return (0, 0) # Unreachable
    

  def in_bounds(self, x: int, y: int, width: int, height: int) -> bool:
    if 0 <= x < width and 0 <= y < height:
      return True
    return False
  

  def find_in_grid(self) -> Tuple[int, int]:
    for y in range(len(grid)):
      for x in range(len(grid[0])):
        if grid[y][x] == '^':
          return (x, y)
        
    raise RuntimeError('Guard was not found in the grid!')


with open(script_dir / 'input.txt') as f:
  grid = [[c for c in line.strip()] for line in f.readlines()]

guard = Guard(grid)

try:
  while True:
    guard.step()
except RuntimeError as e:

  # Guard has left the grid
  print('\n'.join(''.join(row) for row in grid))
  print()

num_spaces = sum([row.count('X') for row in grid])
print(num_spaces)
