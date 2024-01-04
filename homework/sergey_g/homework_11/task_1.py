from abc import abstractmethod


class Book:
    material = 'бумага'
    has_text = True

    def __init__(self, title, author, num_pages, isbn, reserved):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserved = reserved

    @abstractmethod
    def details(self):
        pass


class Novel(Book):
    def __init__(self, title, author, num_pages, isbn, reserved):
        super().__init__(title, author, num_pages, isbn, reserved)

    def details(self):
        if self.reserved:
            print(
                f"Название: {self.title}, Автор: {self.author}, страниц: {self.num_pages}, "
                f"материал: {self.material}, зарезервирована")
        else:
            print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.num_pages}, "
                  f"материал: {self.material}")


class SchoolBook(Book):
    def __init__(self, title, author, num_pages, isbn, reserved, subject, grade, has_exercises):
        super().__init__(title, author, num_pages, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.has_exercises = has_exercises

    def details(self):
        if self.reserved:
            print(
                f"Название: {self.title}, Автор: {self.author}, страниц: {self.num_pages}, "
                f"предмет: {self.subject}, класс: {self.grade}, зарезервирована")
        else:
            print(
                f"Название: {self.title}, Автор: {self.author}, страниц: {self.num_pages}, "
                f"предмет: {self.subject}, класс: {self.grade}")


novel1 = Novel("Идиот", "Достоевский", 553, "987-5-93673-265-2", True)
novel2 = Novel("Преступление и наказание", "Достоевский", 478, "234-5-93233-265-8",
               False)
novel3 = Novel("Мастер и маргарита", "Булгаков", 365, "123-7-95673-265-0", False)
novel4 = Novel("1984", "Оруэлл", 806, "987-5-93673-265-2", True)
novel5 = Novel("Унесенные ветром", True, 305, "334-5-78673-265-8", False)

schoolbook1 = SchoolBook("Алгебра", "Иванов", 223, "678-5-09673-265-8", False,
                         "Математика", 7, False)
schoolbook2 = SchoolBook("История", "Петров", 180, "334-7-56663-265-8", True,
                         "История", 9, True)
schoolbook3 = SchoolBook("География", "Сидоров", 374, "998-3-87673-265-8", False,
                         "География", 8, True)
schoolbook4 = SchoolBook("Биология", "Козлов", 227, "876-8-78679-267-0", False,
                         "Биология", 11, False)
schoolbook5 = SchoolBook("Физика", "Ляпин", 345, "456-1-78673-244-7", False,
                         "Физика", 10, True)

novel1.details()
novel2.details()
novel3.details()
novel4.details()
novel5.details()

schoolbook1.details()
schoolbook2.details()
schoolbook3.details()
schoolbook4.details()
schoolbook5.details()
