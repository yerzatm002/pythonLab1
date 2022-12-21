class Person:
    def __init__(self, age: int, full_name: str):
        self.age = age
        self.full_name = full_name


class Driver(Person):
    def __init__(self, full_name: str, age: int, experience: int):
        Person.__init__(self, age, full_name)
        self.experience = experience

    def __repr__(self):
        return f'{self.full_name} age: {self.age}, with experience {self.experience} years'


class Engine:
    def __init__(self, power: int, company: str):
        self.power = power
        self.company = company

    def __repr__(self):
        return f'{self.company} with power {self.power}'


class Car:
    def __init__(self, car_class: str, engine: Engine, driver: Driver, marka: str):
        self.car_class = car_class
        self.engine = engine
        self.driver = driver
        self.marka = marka

    def start(self) -> None:
        print('Поехали')

    def stop(self) -> None:
        print('Останавливаемся')

    def turn_right(self) -> None:
        print('Поворот направо')

    def turn_left(self) -> None:
        print('Поворот налево')

    def __repr__(self):
        return f'Car: {self.marka} {self.car_class}, Engine: {self.engine}, Driver: {self.driver}'


class Lorry(Car):
    def __init__(self, carrying: int, car_class: str, engine: Engine, driver: Driver, marka: str):
        Car.__init__(self, car_class, engine, driver, marka)
        self.carrying = carrying

    def __repr__(self):
        return f'{self.driver}, {self.marka} {self.car_class}, {self.engine}, {self.carrying}'


class SportCar(Car):
    def __init__(self, speed: float, car_class: str, engine: Engine, driver: Driver, marka: str):
        Car.__init__(self, car_class, engine, driver, marka)
        self.speed = speed

    def __repr__(self):
        return f'{self.driver}, {self.marka} {self.car_class}, {self.engine}, {self.speed}'
