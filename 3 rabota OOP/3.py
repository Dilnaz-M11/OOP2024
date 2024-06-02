# Классы компонентов автомобиля
class Engine:
    def __str__(self):
        return "Engine"

class Transmission:
    def __str__(self):
        return "Transmission"

class Body:
    def __str__(self):
        return "Body"

# Класс CarBuilder
class CarBuilder:
    def __init__(self):
        self.car = None

    def add_engine(self, engine):
        self.car.engine = engine

    def add_transmission(self, transmission):
        self.car.transmission = transmission

    def add_body(self, body):
        self.car.body = body

# Класс CarDirector
class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        self.builder.car = Car()
        self.builder.add_body(Body())
        self.builder.add_engine(Engine())
        self.builder.add_transmission(Transmission())
        return self.builder.car

# Класс Car
class Car:
    def __init__(self):
        self.engine = None
        self.transmission = None
        self.body = None

    def __str__(self):
        return f"{self.engine}, {self.transmission}, {self.body}"

# Конкретные реализации строителей для типов автомобилей
class SedanBuilder(CarBuilder):
    def __init__(self):
        super().__init__()

class SUVBuilder(CarBuilder):
    def __init__(self):
        super().__init__()

class SportsCarBuilder(CarBuilder):
    def __init__(self):
        super().__init__()

# Пример использования
sedan_builder = SedanBuilder()
director = CarDirector(sedan_builder)
sedan = director.construct_car()
print("Создан седан:", sedan)
