# Дана строка. Подсчитать количество содержащихся в ней цифр.

text = input("Введите строку: ")

count = 0

for char in text:
    if char >= '0' and char <= '9':
        count = count + 1

print("Количество цифр в строке:", count)