from pathlib import Path

script_dir = Path(__file__).parent

with open(script_dir / 'input.txt') as f:
  lines = f.readlines()
  turns = []

  for line in lines:
    if line.startswith('L'):
      turns.append(int(line[1:]) * -1)
    else:
      turns.append(int(line[1:]))

dial = 50
num_zeroes = 0

for turn in turns:

  start_at_zero = dial == 0
  partial_turn = turn % 100

  # Any whole turn immediately counts as passing zero
  num_rotations = abs(turn) // 100
  num_zeroes += num_rotations

  # If turning left (-), the mod operator gives a positive number, so we need to adjust
  # -68 % 100 = 32 <-- though the dial math this is used in later still lines up, we need this signed value to check for wrap around
  #  68 % 100 = 68
  if turn < 0 and partial_turn != 0:
    partial_turn -= 100

  dial += partial_turn

  # Now we handle the wrap around. Did this motion pass a zero?
  if dial > 99:
    dial -= 100
    num_zeroes += 1
  elif dial < 0:
    dial += 100

    # If we'ere starting at zero, than ANY left turn will make a wraparound
    # So not having this check would make us double-count
    if not start_at_zero:
      num_zeroes += 1
  elif dial == 0 and not start_at_zero:
      num_zeroes += 1

print(dial, num_zeroes)

