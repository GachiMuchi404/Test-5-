# import random

# class Game:
#     def __init__(self, min_num=1, max_num=100, max_attempts=None):
#         self.min_num = min_num
#         self.max_num = max_num
#         self.max_attempts = max_attempts
#         self.secret_number = random.randint(min_num, max_num)
#         self.attempts = 0

#     def check_guess(self, guess):
#         self.attempts += 1
#         if guess < self.secret_number:
#             return "Загаданное число больше!"
#         elif guess > self.secret_number:
#             return "Загаданное число меньше!"
#         else:
#             return f"Поздравляю! Вы угадали число {self.secret_number} за {self.attempts} попыток."

# class Player:
#     def make_guess(self):
#         while True:
#             try:
#                 return int(input("Введите число: "))
#             except ValueError:
#                 print("Пожалуйста, введите целое число.")

# def main():
#     while True:
#         print("\nДобро пожаловать в игру 'Угадай число'!")
#         difficulty = input("Выберите уровень сложности (1 - легко [1-50], 2 - средне [1-100], 3 - сложно [1-1000]): ")

#         if difficulty == "1":
#             game = Game(1, 50)
#         elif difficulty == "2":
#             game = Game(1, 100)
#         elif difficulty == "3":
#             game = Game(1, 1000)
#         else:
#             print("Некорректный выбор, игра начнётся с диапазоном 1-100.")
#             game = Game()

#         player = Player()
        
#         while True:
#             guess = player.make_guess()
#             result = game.check_guess(guess)
#             print(result)
#             if "Поздравляю" in result:
#                 break

#         replay = input("Хотите сыграть снова? (да/нет): ").lower()
#         if replay != "да":
#             print("Спасибо за игру!")
#             break

# if __name__ == "__main__":
#     main()
