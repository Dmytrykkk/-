import random


def swap_obj(obj1, obj2):
    return obj2, obj1


def fill_array(array_size):
    array = []
    if array_size < 0:
        print("Розмір масиву не може бути від'ємним")
    else:
        array.append(random.randint(1, 9))
        for i in range(array_size - 1):
            element = random.randint(0, 9)
            array.append(element)
    return array


size1 = int(input("Введіть розмір першого числа: "))
size2 = int(input("Введіть розмір другого числа: "))

maximum = max(size1, size2)
add = 0
sign = 0
change = 0

array1 = fill_array(size1)
array2 = fill_array(size2)
array3 = []

while change != 1 and change != 2:
    change = int(input("1 - додати числа \n2 - від першого відняти друге \nВведіть цифру: "))

print("Перший масив:", array1)
print("Другий масив:", array2)

if change == 1:
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

else:
    if size2 > size1 or array2[0] > array1[0]:
        array1, array2 = swap_obj(array1, array2)
        size1, size2 = swap_obj(size1, size2)
        sign = 1

    for k in range(maximum):
        num1 = array1[size1 - 1 - k] if size1 - 1 - k >= 0 else 0
        num2 = array2[size2 - 1 - k] if size2 - 1 - k >= 0 else 0
        num3 = num1 - num2 - add
        if num3 < 0:
            num3 += 10
            add = 1
        else:
            add = 0
        array3.append(num3)

array3.reverse()

print("Результат:", array3)
if sign != 0:
    print("Число від'ємне")
