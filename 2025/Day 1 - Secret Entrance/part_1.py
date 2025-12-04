with open('input.txt') as file:
  lines = file.readlines()
  turns = []

  for line in lines:
    if line.startswith('L'):
      turns.append(int(line[1:]) * -1)
    else:
      turns.append(int(line[1:]))

dial = 50
num_zeroes = 0

for turn in turns:
  dial += (turn % 100)
  if dial > 99:
    dial -= 100
  elif dial < 0:
    dial += 100

  if dial == 0:
    num_zeroes += 1

print(dial, num_zeroes)

