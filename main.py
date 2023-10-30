class Car:
    def __init__(self, model, year, manufacturer, engine_capacity, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price


    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_capacity(self):
        return self.engine_capacity

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_engine_capacity(self, engine_capacity):
        self.engine_capacity = engine_capacity

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price

car1 = Car("some_model", 2020, "lada", 5.0, "red", 100000)
car1.display_data()

print("Производитель:", car1.get_manufacturer())
print("Год выпуска:", car1.get_year())
print("Цена:", car1.get_price())
print("Цвет машины:", car1.get_color())
print("Название модели:", car1.get_model())
print("Объем двигателя:", car1.get_engine_capacity())

car1.set_price(25000)
print("Новая цена:", car1.get_price())
#########################################################
class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price


    def display_data(self):
        print("Название книги:", self.title)
        print("Год выпуска:", self.year)
        print("Издатель:", self.publisher)
        print("Жанр:", self.genre)
        print("Автор:", self.author)
        print("Цена:", self.price)

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    def set_title(self, title):
        self.title = title

    def set_year(self, year):
        self.year = year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_genre(self, genre):
        self.genre = genre

    def set_author(self, author):
        self.author = author

    def set_price(self, price):
        self.price = price

book1 = Book("some_book", 1970, "some_publisher", "some_genre", "some_author", 20000)
book1.display_data()

print("Автор:", book1.get_author())
print("Год выпуска:", book1.get_year())
print("Цена:", book1.get_price())
print("Название книги:", book1.get_title())
print("Жанр:", book1.get_genre())
print("Издатель:", book1.get_publisher())

book1.set_price(1999)
print("Новая цена:", book1.get_price())
###############################################
class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def display_data(self):
        print("Название стадиона:", self.name)
        print("Дата открытия:", self.opening_date)
        print("Страна:", self.country)
        print("Город:", self.city)
        print("Вместимость:", self.capacity)

    def get_name(self):
        return self.name

    def get_opening_date(self):
        return self.opening_date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity

    def set_name(self, name):
        self.name = name

    def set_opening_date(self, opening_date):
        self.opening_date = opening_date

    def set_country(self, country):
        self.country = country

    def set_city(self, city):
        self.city = city

    def set_capacity(self, capacity):
        self.capacity = capacity

    def input_data(self):
        self.name = input("Введите название стадиона: ")
        self.opening_date = input("Введите дату открытия: ")
        self.country = input("Введите страну: ")
        self.city = input("Введите город: ")
        self.capacity = int(input("Введите вместимость: "))

stadium1 = Stadium("some_stadium", "2020.10.28", "some_country", "some_city", 10000)
stadium1.display_data()

print("Страна:", stadium1.get_country())
print("Город:", stadium1.get_city())
print("Название стадиона:", stadium1.get_name())
print("Вместимость:", stadium1.get_capacity())
print("Дата открытия:", stadium1.get_opening_date())

stadium1.set_capacity(60000)
print("Новая вместимость:", stadium1.get_capacity())
