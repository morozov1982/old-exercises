# Генератор числовых последовательностей по введённым пользователем данным

print(
    '''
        Добро пожаловать!
    Вас приветствует генератор числовых последовательностей.
    Введите начальное и кнечные числа последовательности,
    а также интервал между числами.
    Каждый раз после ввода нажимате Enter.
    ''')

first_num = int(input("Введите начальное число: "))
last_num = int(input("Введите конечное число: "))
num_interval = int(input("Введите интервал между числами: "))

num_range = ()
num_range = range(first_num, last_num, num_interval)
print("Ваша последовательность готова:")
print("\t", list(num_range))

input("Нажмите Enter, чтобы выйти.")
