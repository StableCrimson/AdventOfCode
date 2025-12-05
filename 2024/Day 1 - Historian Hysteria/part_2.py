from pathlib import Path

script_dir = Path(__file__).parent

left = []
right = []
similarity = 0

with open(script_dir / 'input.txt') as f:
    contents = f.readlines()

    # For every line "1234    5678" break them up into
    # individual numbers (1234, 5678) and put them in their respective lists
    for line in contents:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

# Calculate the similariry score
for num in left:
    occur = right.count(num)
    similarity += num * occur

print(similarity)
