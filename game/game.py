import random

def get_user_choice():
 while True:
  user_choice = input("Введите свой выбор (камень, ножницы, бумага): ").lower()
  if user_choice in ["камень", "ножницы", "бумага"]:
   return user_choice
  else:
   print("Неверный выбор. Пожалуйста, введите камень, ножницы или бумага.")

def get_computer_choice():
 choices = ["камень", "ножницы", "бумага"]
 return random.choice(choices)

def determine_winner(user_choice, computer_choice):
 print(f"Вы выбрали: {user_choice}")
 print(f"Компьютер выбрал: {computer_choice}")

 if user_choice == computer_choice:
  return "Ничья!"
 elif (
   (user_choice == "камень" and computer_choice == "ножницы") or
   (user_choice == "ножницы" and computer_choice == "бумага") or
   (user_choice == "бумага" and computer_choice == "камень")
 ):
  return "Вы победили!"
 else:
  return "Компьютер победил!"

def play_game():
 user_choice = get_user_choice()
 computer_choice = get_computer_choice()
 winner = determine_winner(user_choice, computer_choice)
 print(winner)

if __name__ == "__main__":
 play_game()
