grid = []

with open("input.txt", 'r') as file:
  lines = file.readlines()
  
  for line in lines:
    grid.append(line.strip()) # Trimming off the whitespace

x_size = len(grid[0])
y_size = len(grid)

# Is the current point on the grid on the edge of it?
def is_on_edge(x, y) -> bool:
  return x in [0, x_size-1] or y in [0, y_size-1]

  
def test_diagonals(x, y):
  
  # If the 'A' is on the edge, then at least 2 of the
  # corners must be out of bounds, and therefore we can't
  # have a match
  if is_on_edge(x, y):
    return False
  
  legal_characters = {'M', 'S'}

  upper_left = grid[y-1][x-1]
  lower_right = grid[y+1][x+1]

  upper_right = grid[y-1][x+1]
  lower_left = grid[y+1][x-1]

  # ? . .
  # . A .
  # . . .
  if upper_left not in legal_characters:
    return False
  
  # ! . .
  # . A .
  # . . ?
  if lower_right != legal_characters.difference(upper_left).pop():
    return False
  
  # ! . ?
  # . A .
  # . . !
  if upper_right not in legal_characters:
    return False
  
  # ! . !
  # . A .
  # ? . !
  if lower_left != legal_characters.difference(upper_right).pop():
    return False
  
  # ! . !
  # . A .
  # ! . !
  return True

def search_grid() -> int:

  matches = 0

  for x in range(x_size):
    for y in range(y_size):

      if grid[y][x] != 'A':
        continue

      matches += 1 if test_diagonals(x, y) else 0

  return matches

print(search_grid())