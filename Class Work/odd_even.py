# odd_even

for number in range(1, 51):

 if number % 2 == 0:
  result = number ** 2
  print(f"Square of even number {number} is {result}", end = (', '))

 else:
  result = number ** 3
  print(f"Cube of odd number {number} is {result}", end = (', '))
  