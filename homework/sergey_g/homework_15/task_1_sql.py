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

# Создание студента
name_stud = 'Tom'
second_name_stud = 'Delonge'
add_stud = 'INSERT INTO students (name, second_name) values (%s, %s)'
cursor.execute(add_stud, (name_stud, second_name_stud))
student_id = cursor.lastrowid
db.commit()

# Создание группы и определения в нее созданного студента
add_stud_group = 'INSERT INTO `groups` (title, start_date, end_date) values (%s, %s, %s)'
cursor.execute(add_stud_group, ('Box car racing', 'feb 2024', 'feb 2024'))
student_group_id = cursor.lastrowid
db.commit()

set_stud_to_group = 'UPDATE students SET group_id = %s where name like %s and second_name like %s'
cursor.execute(set_stud_to_group, (student_group_id, name_stud, second_name_stud))
db.commit()

# Создание предметов
add_subjets = 'INSERT INTO subjets (title) VALUES (%s)'
cursor.execute(add_subjets, ('Punks in the bank',))
subjets_id_1 = cursor.lastrowid
cursor.execute(add_subjets, ('Shit and all that',))
subjets_id_2 = cursor.lastrowid
db.commit()

# Создание занятий для каждого предмета
add_lessons = 'INSERT INTO lessons (title, subject_id) values (%s, %s)'
cursor.executemany(add_lessons, [
    ('gestures in rock', subjets_id_1),
    ('the rules of the circle pit', subjets_id_1),
    ('The materials of the sticks', subjets_id_2),
    ('Tass, triangle and pump', subjets_id_2)
])
lessons_id = cursor.lastrowid
db.commit()

# Создание книг и привязка их к студенту
add_book = 'INSERT INTO books (title, taken_by_student_id) values (%s, %s)'
cursor.executemany(add_book, [
    ('Blibk 182 History', student_id),
    ('The right book', student_id),
])
book_id = cursor.lastrowid
db.commit()

# Поставить студенту оценки для всех созданных занятий
lesson_marks = 'insert into marks (value, lesson_id, student_id) values (%s, %s, %s)'
cursor.executemany(lesson_marks, [
    ('OK', lessons_id, student_id),
    ('FIVE', lessons_id + 1, student_id),
    ('OK', lessons_id + 2, student_id),
    ('FIVE', lessons_id + 3, student_id)
])
db.commit()

# Получить все оценки студента
all_marks_stud = 'SELECT * FROM marks WHERE student_id = %s'
cursor.execute(all_marks_stud, (student_id,))
marks_result = cursor.fetchall()
print(f'{name_stud} {second_name_stud} marks: {marks_result}')

# Получить все книги, которые находятся у студента
all_books_stud = 'SELECT * FROM books WHERE taken_by_student_id = %s'
cursor.execute(all_books_stud, (student_id,))
books_result = cursor.fetchall()
print(f'{name_stud} {second_name_stud} books: {books_result}')

# Получить всю информацию о студенте
all_stud_info = '''
    SELECT * FROM students
    JOIN "groups" ON students.group_id = groups.id
    JOIN books ON students.id = books.taken_by_student_id
    JOIN marks ON marks.student_id = students.id
    JOIN lessons ON marks.lesson_id = lessons.id
    JOIN subjets ON lessons.subject_id = subjets.id
    WHERE name like %s and second_name like %s'''
cursor.execute(all_stud_info, (name_stud, second_name_stud))
stud_info = cursor.fetchall()
print(f'{name_stud} {second_name_stud} all info: {stud_info}')
