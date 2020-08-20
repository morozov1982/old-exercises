# Виселица
#
# Классическая игра "Виселица". Компьютер случайным образом выбирает слово,
# которое игрок должен отгадать буква за буквой. Если игрок не сумеет
# отгадать за отведенное количество попыток, на экране появится фигурка повешенного.

# импорт модуля
import random

# константы
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("ПУПОК", "ПЕРЕСТРОЙКА", "БОБЁР", "МАФИЯ", "БЕЛЛЕТРИСТИКА", "АФОНЯ", "ПЕРЕБОР", "ПРОФИТРОЛИ")

# инициализация переменных
word = random.choice(WORDS) # слово для отгадывания
so_far = "-" * len(word)    # по одному дефису на каждую букву, которую надо отгадать
wrong = 0   # количество ошибок, которые сделал игрок
used = []   #  буквы, которые игрок уже предлагал

print("Дoбpo пожаловать в игру 'Виселица'. Удачи вам!")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nBы уже предлагали следующие буквы:\n", used)
    print("\nОтгаданное вами в слове сейчас выглядит так:\n", so_far)

    guess = input("\n\nВведите букву: ")
    guess = guess.upper()

    while guess in used:
        print("Вы уже предлагали букву", guess)
        guess = input("\n\nВведите букву: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("\nДа! Буква", guess, "есть в слове!")

        # новая строка so_far с отгаданной буквой или буквами
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("\nК сожалению, буквы", guess, "нет в слове.")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nВас повесили!")
else:
    print("\nВы отгадали!")

print("\nБыло загадано слово", word)

input("Нажмите Enter, чтобы выйти.")
