
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
    
    # All of the pages before the current page
    before = set(update[:i])

    if not before.isdisjoint(rule):
      # This update breaks the rules.
      # There are pages before the current page
      # that must come after
      return False

  return True

def correct_update(update: list):
  
  raw_update = set(update)
  corrected_update = []

  while len(raw_update) != 0:
    
    for el in raw_update:
      rule = rules[el]

      # If there are no members of this update that need to be before `el`, then el
      # must be the next valid element. Remove it from the waitlist and put it in the
      # next spot of the corrected update
      if rule.isdisjoint(raw_update):
        raw_update.remove(el)
        corrected_update.append(el)
        break

  return corrected_update

for update in updates:

  # We only care about the invalid updates
  if is_update_valid(update):
    continue

    # This update is invalid! Let's fix it and add the middle page to the total
  corrected_update = correct_update(update)
  middle_sum += int(corrected_update[len(corrected_update)//2])

print(middle_sum)