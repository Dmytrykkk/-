from math import sqrt

def fib (x) :
    if sqrt(5*(x**2)-4) % 1 == 0 or sqrt(5*(x**2)+4) % 1 == 0:
        return True
    else:
        return False
# Перевірка чи є число числом фібоначі

n = int(input('Введіть число n: '))

sum = 1

for i in range(1, n + 1):
    if fib(i):
        sum = sum + i

# Знаходження суми чисел фібоначі, що належать множині дійсних чисел від 1 до n

print(sum)
