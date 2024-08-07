import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv()

# Подключение к базе, через переменные окружения .env
db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True, buffered=True)

# Путь к csv файлу из задания
base_path = os.path.dirname(file)  # noqa: F821
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path_data = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

# Чтение csv файла
with open(file_path_data, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)

    for row in file_data:

        query = """
    SELECT students.name, students.second_name, groups.title, books.title, subjets.title, lessons.title, marks.value
        FROM students
        JOIN groups ON students.group_id = groups.id
        JOIN books ON students.id = books.taken_by_student_id
        JOIN marks ON students.id = marks.student_id
        JOIN lessons ON marks.lesson_id = lessons.id
        JOIN subjets ON lessons.subject_id = subjets.id
        WHERE students.name = %s
        AND students.second_name = %s
        AND groups.title = %s
        AND books.title = %s
        AND subjets.title = %s
        AND lessons.title = %s
        AND marks.value = %s
        """

        values = (
            row['name'],
            row['second_name'],
            row['group_title'],
            row['book_title'],
            row['subject_title'],
            row['lesson_title'],
            row['mark_value']
        )

        cursor.execute(query, values)

        data_result = cursor.fetchall()

        if not data_result:
            print(f"Эти данные отсутствуют в базе: {row}")
        else:
            print(f"Все данные из csv файла присутствуют в базе  {row}")

db.close()
