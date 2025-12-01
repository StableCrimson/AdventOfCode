import re

# This is the pattern we are searching for. You can look at regex101 to test it :)
EXPRESSION = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)"

uncorrupted_hits: list[str] = []
total = 0

with open('input.txt', 'r') as file:

  # Find all matches of `mul(X,Y)`, `do()`, and `don't()` in the file
  matches = re.finditer(EXPRESSION, file.read())
  
  for m in matches:
    uncorrupted_hits.append(m.group())
  
# Now we found the uncorrupted data!
# But there's a catch, we need to filter the 'enabled'
# multiplication instructions first!

# By default, multiplication is enabled
enabled = True

for hit in uncorrupted_hits:

  if hit == 'do()':
    enabled = True
    continue

  if hit == 'don\'t()':
    enabled = False
    continue

  if enabled:

    # Let's say we start with 'mul(123,456)'
    hit = hit.removeprefix('mul(') # Remove the beginning: '123,456)'
    hit = hit.removesuffix(')') # Remove the end: '123,456'

    x, y = hit.split(',') # Split at the comma: '123' '456'

    # Now we have the two numbers!
    total += int(x) * int(y)

print(total)