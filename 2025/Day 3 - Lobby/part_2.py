from pathlib import Path

script_dir = Path(__file__).parent

with open(script_dir / 'input.txt') as f:
  banks = [line.strip() for line in f.readlines()]

def max_joltage(bank: str, num_digits: int, show_work: bool = False) -> int:

  available_length = len(bank)
  needed_digits = num_digits
  window_start = 0
  window_end = available_length - needed_digits - 1
  joltage = ''

  indicator = ' ' * len(bank)

  for _ in range(num_digits):
    
    # If the digits we need is equal to the digits left, then just take them all
    if available_length == needed_digits:
      joltage += bank[window_start:]

      if show_work:

        leading_dashes = '-' * window_start
        trailing_dashes = '-' * (available_length - len(bank[window_start:]))
        window_view = leading_dashes + bank[window_start:] + trailing_dashes

        indicator = indicator[:window_start] + bank[window_start:]

        print()
        print(indicator)
        print(bank)
        print(window_view)
        print()
        print(f'Needed: {needed_digits}, Available: {available_length}, Start: {window_start}, End: {window_end}')
        print('Digits needed == Digits available, consuming rest of bank')
        print()

      break

    window = bank[window_start:window_end+1]
    biggest_digit = max(window)
    joltage += biggest_digit


    needed_digits -= 1
    digit_index = bank.index(biggest_digit, window_start)

    if show_work:

      leading_dashes = '-' * window_start
      trailing_dashes = '-' * (available_length - len(window))
      window_view = leading_dashes + window + trailing_dashes

      indicator = indicator[:digit_index] + biggest_digit + indicator[digit_index+1:]
      
      print()
      print(indicator)
      print(bank)
      print(window_view)
      print()
      print(f'Needed: {needed_digits}, Available: {available_length}, Start: {window_start}, End: {window_end}')
      print()

    local_index = digit_index - window_start
    available_length -= local_index + 1
    window_start = digit_index + 1
    window_size = available_length - needed_digits
    window_end = window_start + window_size

  return int(joltage)

total = 0

for bank in banks:
  joltage = max_joltage(bank, 12, True)
  print(f'\nJoltage for bank \'{bank}\': {joltage}\n')
  total += joltage

print(total)
