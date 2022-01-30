# Debugging FizzBuzz

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz\n\n")
  elif number % 3 == 0:
    print("\nFizz\n\n")
  elif number % 5 == 0:
    print("\nBuzz")
  else:
    print(number)
