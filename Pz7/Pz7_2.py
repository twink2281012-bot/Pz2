# Дана строка-предложение на русском языке. Вывести самое длинное слово в
# предложении. Если таких слов несколько, то вывести первое из них. Словом считать
# набор символов, не содержащий пробелов, знаков препинания и ограниченный
# пробелами, знаками препинания или началом/концом строки.

sentence = input("Введите предложение на русском языке: ")

punctuation = ".,!?-:;()"
for p in punctuation:
    sentence = sentence.replace(p, " ")

words = sentence.split()

longest_word = ""
max_length = 0

for word in words:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word

print("Самое длинное слово:", longest_word)
print("Длина:", max_length)