def fizzbuzz(number: int) -> int or str:
  if (number == 0):
    return 0

  if (number % 3 == 0 and number % 5 == 0):
    return 'fizzbuzz'

  if (number % 3 == 0):
    return 'fizz'

  if (number % 5 == 0):
    return 'buzz'

  return number

def run_fizzbuzz(count: int) -> None:
  for x in range(count):
    print(f'number: {x}: {fizzbuzz(x)}')

run_fizzbuzz(16)
