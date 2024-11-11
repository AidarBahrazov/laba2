from datetime import date, datetime

def calculate_age(birthdate_str):
  try:
    birthdate = datetime.strptime(birthdate_str, "%d %m %Y").date()
  except ValueError:
    raise ValueError("Неверный формат даты рождения. Используйте формат день месяц год, через пробел (например, 24 03 2004).")

  today = date.today()
  age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
  return age

if __name__ == "__main__":
  birthdate_str = input("Введите дату рождения в формате день месяц год, через пробел (например, 24 03 2004): ")
  try:
    age = calculate_age(birthdate_str)
    print(f"Ваш возраст: {age} лет")
  except ValueError as e:
    print(f"Ошибка: {e}")

