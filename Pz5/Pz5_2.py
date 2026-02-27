# Описать функцию ShiftRight3(A, B, C), выполняющую правый циклический сдвиг:
# значение A переходит в B, значение B — в C, значение C — в A (A, B, C —
# вещественные параметры, являющиеся одновременно входными и выходными). С
# помощью этой функции выполнить правый циклический сдвиг для двух данных
# наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2).

def ShiftRight3(A, B, C):
    print(f"    Вызвана функция ShiftRight3 с числами: A={A}, B={B}, C={C}")

    temp = C

    C = B
    B = A
    A = temp

    print(f"    После сдвига: A={A}, B={B}, C={C}")
    print()

    return A, B, C


print  ("Программа для правого циклического сдвига трех чисел")
print("-" * 50)

print("Введите первый набор чисел (A1, B1, C1):")
A1 = float(input("A1 = "))
B1 = float(input("B1 = "))
C1 = float(input("C1 = "))

print("\nВведите второй набор чисел (A2, B2, C2):")
A2 = float(input("A2 = "))
B2 = float(input("B2 = "))
C2 = float(input("C2 = "))

print("\n" + "=" * 50)
print("РЕЗУЛЬТАТЫ:")
print("=" * 50)

print("Первый набор чисел:")
print(f"Исходные: A1={A1}, B1={B1}, C1={C1}")
A1_new, B1_new, C1_new = ShiftRight3(A1, B1, C1)
print(f"Результат: A1={A1_new}, B1={B1_new}, C1={C1_new}")

print()

print("Второй набор чисел:")
print(f"Исходные: A2={A2}, B2={B2}, C2={C2}")
A2_new, B2_new, C2_new = ShiftRight3(A2, B2, C2)
print(f"Результат: A2={A2_new}, B2={B2_new}, C2={C2_new}")