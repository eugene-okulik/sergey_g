# Задание
# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры (объекты) цветов разных видов.
# Собрать букет (букет - еще один класс) с определением его стоимости.
# В букете цветы пусть хранятся в списке. Это будет список объектов.
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни)
# (и это тоже метод).

class Flower:
    def __init__(self, color, freshness, stem_length, price, lifespan):
        self.color = color
        self.freshness = freshness
        self.stem_length = stem_length
        self.price = price
        self.lifespan = lifespan


class Rose(Flower):
    def __init__(self, color, freshness, stem_length, price, lifespan, is_fragrant):
        super().__init__(color, freshness, stem_length, price, lifespan)
        self.is_fragrant = is_fragrant


class Tulip(Flower):
    def __init__(self, color, freshness, stem_length, price, lifespan, is_double):
        super().__init__(color, freshness, stem_length, price, lifespan)
        self.is_double = is_double


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def calculate_cost(self):
        total_cost = 0
        for flower in self.flowers:
            total_cost += flower.price
        return total_cost

    def average_lifespan(self):
        total_lifespan = 0
        for flower in self.flowers:
            total_lifespan += flower.lifespan
        return total_lifespan / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda x: x.freshness, reverse=True)

    def sort_by_color(self):
        self.flowers.sort(key=lambda x: x.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda x: x.stem_length, reverse=True)

    def sort_by_cost(self):
        self.flowers.sort(key=lambda x: x.price, reverse=True)

    def search_by_lifespan(self, lifespan):
        return [flower for flower in self.flowers if flower.lifespan == lifespan]


red_rose = Rose("Красная роза", 90, 20, 5, 7, True)
yellow_tulip = Tulip("Желтый тюльпан", 80, 15, 3, 5, False)
white_rose = Rose("Белая роза", 95, 25, 6, 6, True)

bouquet = Bouquet([red_rose, yellow_tulip, white_rose])

print(f"Полная стоимость букета:", bouquet.calculate_cost(), "руб.")
print("Средний срок жизни букета:", int(bouquet.average_lifespan()), "дней")

bouquet.sort_by_freshness()

print("Цветы отсортированы по свежести:", [flower.color for flower in bouquet.flowers])
print("Цветы со сроком жизни 6 дней:", [flower.color for flower in bouquet.search_by_lifespan(6)])
