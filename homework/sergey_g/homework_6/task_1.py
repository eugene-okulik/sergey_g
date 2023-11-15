# Задание №1
# Напишите программу, которая добавляет ‘ing’ к каждому слову в тексте “Etiam tincidunt neque erat, quis molestie enim
# imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”
# и после этого выводит получившийся текст на экран.

text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, '
    + 'facilisis vitae semper at, dignissim vitae libero'
)
print(f'Исходная версия текста: {text}')

words = text.split()
result = []

for word in words:
    if word.endswith(','):
        word = word[:-1] + 'ing,'
    elif word.endswith('.'):
        word = word[:-1] + 'ing.'
    else:
        word = word + 'ing'
    result.append(word)

result_text = ' '.join(result)
print(f'Редактированный текст : {result_text}')
