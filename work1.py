import random


def fill_array(array_size):
    if array_size < 0:
        print("Розмір масиву не може бути від'ємним")
    else:
        array = [random.randint(1, 9)]
        for i in range(array_size - 1):
            element = random.randint(0, 9)
            array.append(element)
    return array


size1 = int(input("Введіть розмір першого числа: "))
size2 = int(input("Введіть розмір другого числа: "))

maximum = max(size1, size2)
add = 0
sign = 0

array1 = fill_array(size1)
array2 = fill_array(size2)
array3 = []

print("Перший масив:", array1)
print("Другий масив:", array2)

for k in range(maximum):
    num1 = array1[size1 - 1 - k] if size1 - 1 - k >= 0 else 0
    num2 = array2[size2 - 1 - k] if size2 - 1 - k >= 0 else 0
    num3 = num2 + num1 + add
    if num3 > 9:
        num3 = num3 % 10
        add = 1
    else:
        add = 0
    array3.append(num3)
if add != 0:
    array3.append(add)

array3.reverse()

print("Результат:", array3)
if sign != 0:
    print("Число від'ємне")
