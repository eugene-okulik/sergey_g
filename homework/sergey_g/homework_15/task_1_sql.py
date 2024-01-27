"""
Все действия с базой данных из прошлого домашнего задания напишите с помощью Python.
При получении данных, распечатывайте эти данные.
"""

import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# Создание группы
cursor.execute(
    """INSERT INTO "groups"(title, start_date, end_date) VALUES ('Box car racing', 'jan 2024', 'feb 2024')""")
db.commit()

# Создание студента
cursor.execute("INSERT INTO students (name, second_name) VALUE ('Tom', 'Delonge')")
db.commit()

# Создание предметов
subjects = [
    ("Punks in the bank",),
    ("Shit and all that",),
]
cursor.executemany("INSERT INTO subjets(title) VALUES(%s)", subjects)
db.commit()

# Создание занятий для каждого предмета
lessons = [
    ("gestures in rock", "236"),
    ("the rules of the circle pit", "236"),
    ("The materials of the sticks", "237"),
    ("Tass, triangle and pump", "237"),
]
cursor.executemany(
    "INSERT INTO lessons(title, subject_id) VALUES(%s, %s)", lessons)
db.commit()

# Создание книг и привязка их к студенту
books = [
    ("Blibk 182 History»", 183),
    ("the right book", 183),
]
cursor.executemany(
    "INSERT INTO books(title, taken_by_student_id) VALUES(%s, %s)", books)
db.commit()

# Поставить студенту оценки для всех созданных занятий
marks = [("OK", 274, 183), ("FIVE", 275, 183), ("OK", 276, 183), ("FIVE", 277, 183)]
cursor.executemany(
    "INSERT INTO marks(value, lesson_id, student_id) VALUES(%s, %s, %s)", marks)
db.commit()

# Получить все оценки студента
cursor.execute("SELECT * FROM marks WHERE student_id = 183")
result = cursor.fetchall()
for mark in result:
    print(mark)

# Получить все книги, которые находятся у студента
cursor.execute("SELECT * FROM books WHERE taken_by_student_id = 183")
result = cursor.fetchall()
for book in result:
    print(book)

# Получить всю информацию о студенте
cursor.execute(
    """
    SELECT * FROM students
    JOIN "groups" ON students.group_id = groups.id
    JOIN books ON students.id = books.taken_by_student_id
    JOIN marks ON marks.student_id = students.id
    JOIN lessons ON marks.lesson_id = lessons.id
    JOIN subjets ON lessons.subject_id = subjets.id
    WHERE students.id = 183;
    """
)
stud_info = cursor.fetchall()
for info in stud_info:
    print(info)
