import random

def find_multiples(x, numbers):
  is_multiple = lambda num: num % x == 0
  multiples = list(filter(is_multiple, numbers))
  return multiples

if __name__ == "__main__":
  while True:
    try:
      x = int(input("Введите число от 1 до 9: "))
      if 1 <= x <= 9:
        break
      else:
        print("Ошибка: Введите число от 1 до 9.")
    except ValueError:
      print("Ошибка: Введите число.")

  numbers = random.sample(range(201), 10) 
  print(f"Сгенерированный список: {numbers}")
  multiples = find_multiples(x, numbers)
  print(f"Числа, кратные {x}: {multiples}")


