import random


def generate_mass(n):
    """
    Створення та виведення масиву з n рандомних чисел
    """
    mass = set()

    for i in range(n):
        x = random.randint(0, 100)
        mass.add(x)

    return mass


def generate_random_dict(n):
    """
    Створення та виведення словника з n рандомних елементів існуючого словника
    """
    var = {
        "Київ": 1, "Луцьк": 12, "Івано-Франківськ": 123, "Житомир": 43,
        "Львів": 2, "Херсон": 31, "Миколаїв": 8, "Одеса": 1,
        "Харків": 3, "Донецьк": 5, "Тернопіль": 7, "Дніпро": 64,
        "Умань": 98, "Луганск": 41, "Запоріжжя": 23, "Полтава": 241

    }
    random_items = random.sample(list(var.items()), n)
    return dict(random_items)


def generate_random_list(n):
    """
    Створення та виведення списку з n рандомних чисел
    """
    random_list = []

    for i in range(n):
        random_list.append(random.randint(0, 100))

    return random_list


def sort_duo_dict(obj1, obj2):
    """
    Об'єднання двух словників та сортування
    """
    return {k: v for k, v in sorted({**obj1, **obj2}.items(), key=lambda item: item[1])}


def slice_dict(obj1, obj2):
    """
    Зріз двух словників
    """
    if len(obj2) > len(obj1):
        obj1, obj2 = obj2, obj1

    dict_slice = {k: obj1[k] for k in obj1.keys() & obj2.keys()}

    return dict_slice


choose1 = 0
while choose1 not in [1, 2, 3]:
    choose1 = int(input(
        "Оберіть тип об'єктів, що хочете створити: \n 1 - масив \n 2 - словник \n 3 - список \n Введіть цифру: "))

size1 = 0
size2 = 0
while not (1 <= size1 <= 16):
    size1 = int(input("Введіть розмір першого об'єкту (не має перевизувати 16): "))
while not (1 <= size2 <= 16):
    size2 = int(input("Введіть розмір другого об'єкту (не має перевищувати 16): "))

if choose1 == 1:
    object1 = generate_mass(size1)
    object2 = generate_mass(size2)
elif choose1 == 2:
    object1 = generate_random_dict(size1)
    object2 = generate_random_dict(size2)
else:
    object1 = generate_random_list(size1)
    object2 = generate_random_list(size2)

print("Перший об'єкт:\n", object1, "\nДругий об'єкт:\n", object2,
      "\nОберіть дію:\n1 - додавання елементу до першого об'єкту\n2 - видалення елементу першого об'єкту"
      "\n3 - Зріз двух об'єктів \n4 - об'єдання двух об'єктів та сортування отриманого")

choose2 = 0
while choose2 not in [1, 2, 3, 4]:
    choose2 = int(input("Введіть цифру: "))

if choose2 == 1:
    if choose1 == 1:
        value = int(input("Введіть новий елемент: "))
        object1.add(value)
    elif choose1 == 2:
        key = input("Введіть ключ: ")
        value = int(input("Введіть значення: "))
        object1[key] = value
    else:
        value = int(input("Введіть новий елемент: "))
        object1.append(value)
    print("Результат:\n", object1)
elif choose2 == 2:
    if choose1 == 1:
        value = int(input("Введіть елемент, що бажаєте видалити: "))
        object1.discard(value)
    elif choose1 == 2:
        key = input("Введіть ключ елемента, що бажаєте видалити: ")
        if key in object1:
            del object1[key]
    else:
        value = int(input("Введіть елемент, що бажаєте видалити: "))
        if value in object1:
            del object1[value]
    print("Результат:\n", object1)
elif choose2 == 3:
    if choose1 == 2:
        object3 = slice_dict(object1, object2)
    else:
        object3 = list(set(object1) & set(object2))
    print("Результат:\n", object3)
else:
    if choose1 == 2:
        object3 = sort_duo_dict(object1, object2)
    else:
        object3 = sorted(list(object1) + list(object2))
    print("Результат:\n", object3)
