INSERT INTO `groups`(id, title, start_date, end_date) VALUES (182, 'BLINK', 'jan 2024', 'feb 2024' )

INSERT INTO students (name, second_name, group_id) VALUE ('Travis', 'Barker', '182')

INSERT INTO subjets (id, title) VALUE ('100', 'punk rock for intellectuals')
INSERT INTO subjets (id, title) VALUE ('99', 'The art of playing the drums')

INSERT INTO lessons (id, title, subject_id) VALUE ('7', 'gestures in rock','99')
INSERT INTO lessons (id, title, subject_id) VALUE ('8', 'the rules of the circle pit','99')
INSERT INTO lessons (id, title, subject_id) VALUE ('9', 'paradidles','100')
INSERT INTO lessons (id, title, subject_id) VALUE ('10', 'The materials of the sticks','100')

INSERT INTO books  (id, title, taken_by_student_id) VALUE ('5', 'Just Kids','219')
INSERT INTO books  (id, title, taken_by_student_id) VALUE ('6', 'The philosophy of punk. More than Noise!','219')

INSERT INTO marks  (id, value, lesson_id, student_id) VALUE ('14', '5','7', '219')
INSERT INTO marks  (id, value, lesson_id, student_id) VALUE ('15', '5','8', '219')
INSERT INTO marks  (id, value, lesson_id, student_id) VALUE ('16', '5','9', '219')
INSERT INTO marks  (id, value, lesson_id, student_id) VALUE ('17', '5','10', '219')

SELECT * FROM marks WHERE student_id = 219 
SELECT * FROM books WHERE taken_by_student_id = 219

SELECT * FROM students
JOIN `groups` ON students.group_id = groups.id
JOIN books ON students.id = books.taken_by_student_id
JOIN marks ON marks.student_id = students.id
JOIN lessons ON marks.lesson_id = lessons.id
JOIN subjets ON lessons.subject_id = subjets.id
WHERE students.id = 219
