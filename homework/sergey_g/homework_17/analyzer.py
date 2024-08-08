import os
import argparse


def find_text_in_logs(directory, search_text):
    results = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                for line_number, line in enumerate(file, start=1):
                    if search_text in line:
                        context = get_context(line, search_text)
                        results.append((filename, line_number, context))

    return results


def get_context(line, search_text):
    index = line.find(search_text)

    start_index = max(index - 5 * len(' ') - 5, 0)  # 5 пробелов до
    end_index = min(index + len(search_text) + 5 * len(' ') + 5, len(line))  # 5 пробелов после

    context = line[start_index:end_index].replace(search_text, f"\033[91m{search_text}\033[0m")
    return context


def main():
    parser = argparse.ArgumentParser(description='Поиск текста в логах.')
    parser.add_argument('directory', type=str, help='Полный путь к папке с логами')
    parser.add_argument('--text', required=True, type=str, help='Текст для поиска в логах')

    args = parser.parse_args()
    directory = args.directory
    search_text = args.text

    # Проверка на существование директории
    if not os.path.isdir(directory):
        print(f'Ошибка: Директория {directory} не существует.')
        return

    results = find_text_in_logs(directory, search_text)

    if results:
        for filename, line_number, context in results:
            print(f'Файл: {filename}, Строка: {line_number}')
            print(f'Контекст: {context}')
    else:
        print('Текст не найден.')


if __name__ == '__main__':
    main()

# Команда для запуска python analyzer.py C:\user\data\logs --text WARN
