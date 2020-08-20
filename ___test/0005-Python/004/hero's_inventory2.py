# Арсенал героя 2.0
# Демонстрирует работу с кортежами

# создадим кортеж с несколькими элементами и выведем его с помощью цикла for
inventory = ("меч",
             "кольчуга",
             "щит",
             "целебное снадобье")
print("\nИтак, в вашем арсенале:")

for item in inventory:
    print("  ", item)

input("\nНажмите Enter, чтобы продолжить.")

# найдем длину кортежа
print("Сейчас в вашем распоряжении", len(inventory), "предмета/-ов.")
input("\nНажмите Enter, чтобы продолжить.")

# проверка на принадлежность кортежу с помощью in
if "целебное снадобье" in inventory:
    print("Вы ещё поживёте и повоюете.")

# вывод одного элемента с определенным индексом
index = int(input("\nВведите индекс одного из предметов арсенала: "))
print("Под индексом", index, "в арсенале находится", inventory[index])

# отобразим срез
start = int(input("\nВведите начальный индекс среза: "))
finish = int(input("Введите конечный индекс среза: "))
print("Срез invetory[", start, ":", finish, "] - это", end=" ")
print(inventory[start:finish])

input("\nНажмите Enter, чтобы продолжить.")