from abc import ABC, abstractmethod

# Абстрактная фабрика
class CarFactory(ABC):
    @abstractmethod
    def produce_car(self):
        pass

# Конкретная реализация ElectricCarFactory
class ElectricCarFactory(CarFactory):
    def produce_car(self):
        return ElectricCar()

# Конкретная реализация PetrolCarFactory
class PetrolCarFactory(CarFactory):
    def produce_car(self):
        return PetrolCar()

# Конкретная реализация HybridCarFactory
class HybridCarFactory(CarFactory):
    def produce_car(self):
        return HybridCar()

# Абстрактный класс Car
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

# Реализация ElectricCar
class ElectricCar(Car):
    def drive(self):
        print("Driving an electric car.")

# Реализация PetrolCar
class PetrolCar(Car):
    def drive(self):
        print("Driving a petrol car.")

# Реализация HybridCar
class HybridCar(Car):
    def drive(self):
        print("Driving a hybrid car.")

# Использование абстрактной фабрики для создания автомобилей
electric_factory = ElectricCarFactory()
petrol_factory = PetrolCarFactory()
hybrid_factory = HybridCarFactory()

electric_car = electric_factory.produce_car()
petrol_car = petrol_factory.produce_car()
hybrid_car = hybrid_factory.produce_car()

electric_car.drive()
# Вывод: Driving an electric car.
petrol_car.drive()
# Вывод: Driving a petrol car.
hybrid_car.drive()
# Вывод: Driving a hybrid car.
