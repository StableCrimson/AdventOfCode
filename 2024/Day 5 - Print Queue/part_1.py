
'''
This will contain all of the rules. Formatted X: [Y, Z]
Where X is a page and Y, Z, etc. are all of the pages
that must NOT come before it in order for the update to be valid
'''
rules = {}
updates = []
middle_sum = 0

with open('input.txt', 'r') as file:
  contents = file.readlines()

  for line in contents:

    # Skip over empty lines
    if line.strip() == '':
      continue

    # Is it a rule?
    if '|' in line:
      x, y = line.strip().split('|')

      if rules.get(x) is None:
        rules[x] = {y}
      else:
        rules[x].add(y)

      continue

    # It's not a rule, it's an update
    updates.append(line.strip().split(','))

def is_update_valid(update: list) -> bool:

  for i in range(len(update)):
    rule = rules.get(update[i])
    
    before = set(update[:i])

    # This update breaks the rules
    if not before.isdisjoint(rule):
      return False

  return True

for update in updates:
  if is_update_valid(update):
    # The update is valid! Get the middle page number add it to the total
    middle_sum += int(update[len(update)//2])

print(middle_sum)