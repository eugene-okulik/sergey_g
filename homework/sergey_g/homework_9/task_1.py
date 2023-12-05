# Задание № 1
# Обработка даты
# Дана такая дата: "Jan 15, 2023 - 12:05:33"
# Преобразуйте эту дату в питоновский формат, после этого:
# 1. Распечатайте полное название месяца из этой даты
# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"

from datetime import datetime

original_date = "Jan 15, 2023 - 12:05:33"
date = datetime.strptime(original_date, "%b %d, %Y - %H:%M:%S")
print(date.strftime("%B"))
print(date.strftime("%d.%m.%Y, %H:%M"))
