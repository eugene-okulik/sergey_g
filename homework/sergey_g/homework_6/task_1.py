# Задание №1
# Напишите программу, которая добавляет ‘ing’ к каждому слову в тексте “Etiam tincidunt neque erat, quis molestie enim
# imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”
# и после этого выводит получившийся текст на экран.

text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, ' \
       'facilisis vitae semper at, dignissim vitae libero'
print(text)

symbol_del_1 = ','
symbol_del_2 = '.'
not_symbol_1 = text.replace(symbol_del_1, '')
new_text = not_symbol_1.replace(symbol_del_2, '')

words = new_text.split()

for i in range(len(words)):
    words[i] += 'ing'

new_text = ' '.join(words)

text = new_text.replace("nisling", "nisling,")
text = text.replace("ating", "ating,")
fin_text = text.replace("veling", "veling.")

print(fin_text)
