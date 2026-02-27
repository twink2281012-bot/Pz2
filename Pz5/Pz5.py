# Найти сумму чисел ряда 1,2,3,...,60 с использованием функции нахождения суммы.
# Использовать локальные переменные.

def find_sum():
    n = 60
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total


result = find_sum()

print("Сумма чисел от 1 до 60 равна:", result)

try:
    print(n)
except NameError:
    print("Переменная n не доступна здесь - она локальная внутри функции")