number = 23
guess = int(input('Введите целое число: '))

if guess == number:
    print('Поздравляю, вы угадали, ') # здесь начинается новый блок
    print('(хотя и не выиграли никакого приза!)') # здесь заканчивается новы блок
elif guess < number:
    print('Нет, загаданное число немного больше этого.') # ещё один блок
    # внутри блока можно выполнять всё, что угодно ...
else:
    print('Нет, загаданное число немного меньше этого.')
    # чтобы попасть сюда, guess должно быть больше, чем number

print('Завершено')
# это последнее выражение выполняется всегда после выполнения оператора if