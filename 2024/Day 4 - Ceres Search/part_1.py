grid = []
TARGET = 'XMAS'

with open("input.txt", 'r') as file:
  lines = file.readlines()
  
  for line in lines:
    grid.append(line.strip()) # Trimming off the whitespace

x_size = len(grid[0])
y_size = len(grid)

# Check if the next spot we want to check is going to be within the bounds of the grid
def next_step_in_bounds(x, y, x_step, y_step) -> bool:

  next_x = x + x_step
  next_y = y + y_step

  if next_x < 0 or next_x >= x_size:
    return False
  
  if next_y < 0 or next_y >= y_size:
    return False
  
  return True

def find_match(index, x, y, x_step, y_step) -> int:

  # We didn't find the character we were looking for. This direction doesn't have a match
  if grid[y][x] != TARGET[index]:
    return 0

  # We matched AND it's the last character, this search found 'XMAS'!
  if grid[y][x] == TARGET[-1]:
    return 1

  # We matched and it's not the last character, but will the next spot be out of bounds?
  if not next_step_in_bounds(x, y, x_step, y_step):
    return 0
  
  # Nope! It's in bounds, so let's check it next
  return find_match(index+1, x+x_step, y+y_step, x_step, y_step)
  
def search_grid() -> int:

  matches = 0

  for x in range(x_size):
    for y in range(y_size):

      matches += find_match(0, x, y, -1,  0) # Left
      matches += find_match(0, x, y,  1,  0) # Right
      matches += find_match(0, x, y,  0, -1) # Up
      matches += find_match(0, x, y,  0,  1) # Down

      # Diagonal
      matches += find_match(0, x, y, -1, -1)
      matches += find_match(0, x, y, -1,  1)
      matches += find_match(0, x, y,  1, -1)
      matches += find_match(0, x, y,  1,  1)

  return matches

print(search_grid())