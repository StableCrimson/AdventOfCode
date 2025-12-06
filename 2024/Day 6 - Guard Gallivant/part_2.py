from pathlib import Path
from typing import List, Tuple
from enum import Enum
from copy import deepcopy

script_dir = Path(__file__).parent

class Direction(Enum):
  Up = 1
  Down = 2
  Left = 4
  Right = 8

NEXT_DIRECTION = { 
  'Up': Direction.Right, 
  'Down': Direction.Left, 
  'Left': Direction.Up, 
  'Right': Direction.Down 
}

class Guard:

  x: int
  y: int
  direction: Direction
  grid: List[List[str]]
  path: List[List[int]]
  left_grid: bool
  stuck_in_loop: bool


  def __init__(self, grid: List[List[str]]):
    self.grid = grid
    self.x, self.y = self.find_in_grid()
    self.direction = Direction.Up
    self.left_grid = False
    self.stuck_in_loop = False
    self.path = [([0] * len(self.grid[0])).copy() for _ in range(len(self.grid))]


  def __str__(self) -> str:
    return f'X: {self.x:03}, Y: {self.y:03}, Direction: {self.direction.name}, Left Grid: {self.left_grid}, Stuck in Loop: {self.stuck_in_loop}'


  def step(self, just_turned: bool = False):

    next_pos = self.next_position()

    if just_turned:
      self.grid[self.y][self.x] = 'T'
    else:
      self.grid[self.y][self.x] = 'X'

    if self.path[self.y][self.x] & self.direction.value != 0:
      self.stuck_in_loop = True
      return

    # Record the directions we have traversed this cell in.
    # Each cardinal direction is a single bit, since we could possible traverse a cell in more than one direction
    # Ex: We enter a cell from the left, and later in the path we also enter that cell from the top
    self.path[self.y][self.x] |= self.direction.value

    if not self.in_bounds(*next_pos, len(self.grid[0]), len(self.grid)):
      self.left_grid = True
      return
    
    if self.grid[next_pos[1]][next_pos[0]] in ['#', 'O']:
      self.direction = NEXT_DIRECTION[self.direction.name]
      self.step(True)
      return

    self.x = next_pos[0]
    self.y = next_pos[1]


  def traverse(self):
    while not (self.left_grid or self.stuck_in_loop):
      self.step()


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
    for y in range(len(self.grid)):
      for x in range(len(self.grid[0])):
        if self.grid[y][x] == '^':
          return (x, y)
        
    raise RuntimeError('Guard was not found in the grid!')

  def print_path(self):
    for x in range(len(self.grid[0])):
      for y in range(len(self.grid)):

        cell = grid[y][x]

        # Empty spaces or obstacles
        if cell in ['.', '#', 'O']:
          print(cell, end='')
          continue

        # Guard
        if x == self.x and y == self.y:
          if self.direction == Direction.Up:
            print('^', end='')
          elif self.direction == Direction.Down:
            print('v', end='')
          elif self.direction == Direction.Left:
            print('<', end='')
          else:
            print('>', end='')
          continue

        # Edge case for properly rendering cells which we've only entered in one direction but left via turn
        if cell == 'T':
          print('+', end='')
          continue

        # Otherwise, we've traversed this cell
        vertical = (self.path[y][x] & 0b0011) != 0
        horizontal = (self.path[y][x] & 0b1100) != 0

        if vertical and horizontal:
          print('+', end='')
        elif vertical:
          print('-', end='')
        else:
          print('|', end='')

      print()


with open(script_dir / 'input.txt') as f:
  grid = [[c for c in line.strip()] for line in f.readlines()]


def place_obstacle(x: int, y: int, grid: List[List[str]]):
  if grid[y][x] not in ['#', 'O', '^']:
    grid[y][x] = 'O'


num_loops = 0

for x in range(len(grid[0])):
  for y in range(len(grid)):
    new_grid = deepcopy(grid)
    place_obstacle(x, y, new_grid)

    guard = Guard(new_grid)
    guard.traverse()

    if guard.stuck_in_loop:
      print(f'Placing an obstable at ({x:03}, {y:03}) places the guard in a loop')
      guard.print_path()
      num_loops += 1


print(f'There are {num_loops} loops we can create by placing an obstacle in the grid at an arbitrary position')
