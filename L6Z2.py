#2.Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
#Значения данных атрибутов должны передаваться при создании экземпляра класса.
#Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
#Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу метода.
#Например: 20м * 5000м * 25кг * 5см = 12500 т
class Road:
    _length = None
    _width = None
    __mass_of_asphalt = 25 #по условию 25 кг
    _thickness = 5 #по условию 5 см
    def __init__(self, lenghth, width):
        self._length = lenghth
        self._width = width
    def calculate(self):
        return self._length * self._width * self.__mass_of_asphalt * self._thickness / 1000 #для перевода в тонны
roads_of_Moscow_region = Road(lenghth=20, width=5000)
print(roads_of_Moscow_region.calculate())
