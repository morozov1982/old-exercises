# Анаrраммы CWord JumЬle)2
#
# Компьютер выбирает какое-пибо слово и хаотически переставляет его буквы
# Задача иrрока - восстановить исходное слово

import random

# создадим последовательность слов, из которых компьютер будет выбирать
WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")

# случайным образом выберем из последовательности одно слово
word = random.choice(WORDS)

# создадим переменную, с которой будет затем сопоставлена версия игрока
correct = word

# создадим анаграмму выбранного слова, в которой буквы будут расставлены хаотично
jumble = ""

# количество попыток, количество очков, количество букв в слове
tries = 0
points = 100
letters = len(word)

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# начало игры
print(
    '''
        Добро пожаловать в игру "Анаграммы"!
        
    Надо переставить буквы так, чтобы получилось осмысленное слово.
    В начале вам даётся 100 очков,
    с каждой неверной попыткой их количество сокращается.

    Если вам нужна подсказка, напишите "HELP".
    
   (Для выхода нажмите Enter, не вводя своей версии.)
    '''
)
print("Вот анаграмма:", jumble)

guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != correct and guess != "":
    if guess == "HELP":
        print("====================**********")
        print("Слово начинается на:", correct[:tries])
        print("====================**********")
    else:
        print("\nК сожалению, вы не правы.")
    tries += 1
    points = 100 - int(100 / letters * tries)
    print("=========================")
    print("У вас", points, "очков.")
    print("=========================")
    print('Если вам нужна подсказка, напишите "HELP".\n')
    guess = input("Попробуйте отгадать исходное слово: ")

if guess == correct:
    print("\nДа, именно так! Вы отгадали!\n")
    print("У вас", points, "очков.")

print("Спасибо за игру.")

input("\n\nНажмите Enter, чтобы выйти.")