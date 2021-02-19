#4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
class Car:
    speed = None
    color = None
    name = None
    is_police = False
    def __init__(self, speed, name, colour, is_police = False):
        self.speed = speed
        self.name = name
        self.color = colour
        self.is_police = is_police
    def go(self):
        return('The car went')
    def stop(self):
        return('The car stop')
    def turn(self):
        return('The car turned to...')