left = []
right = []
total_dist = 0

with open("input.txt", 'r') as f:
    contents = f.readlines()

    # For every line "1234    5678" break them up into
    # individual numbers (1234, 5678) and put them in their respective lists
    for line in contents:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

# Sort the lists so the partner numbers will have the same indices
left.sort()
right.sort()

# Start summing up the differences in the numbers
for a, b in zip(left, right):
    total_dist += abs(a-b)

print(total_dist)