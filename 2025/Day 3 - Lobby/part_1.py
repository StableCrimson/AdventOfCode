with open('input.txt') as f:
  banks = [line.strip() for line in f.readlines()]

def max_joltage(bank: str) -> int:

  biggest_digit = max(bank[:-1])
  _, rest = bank.split(biggest_digit, 1)
  second_biggest_digit = max(rest)

  max_joltage = int(biggest_digit + second_biggest_digit)
  return max_joltage

total = sum(max_joltage(bank) for bank in banks)
print(total)

