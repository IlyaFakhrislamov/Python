'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Скорость {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} - {self.speed}')
        if self.speed > 40:
            return f'{self.name} скорость превышена'

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} - {self.speed}')
        if self.speed > 60:
            return f'{self.name} скорость превышена'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейский автомобиль'
        else:
            return f'{self.name} не полицейский автомобиль'

ferrari = SportCar(100, 'Красный', 'Ferrari', False)
kia = TownCar(30, 'Желтый', 'Kia', False)
lada = WorkCar(70, 'Зеленый', 'Lada', False)
lamborgini = PoliceCar(110, 'Черный',  'Lamborgini', True)

print(lada.turn_left())
print(kia.turn_right())
print(ferrari.stop())
print(f'{lamborgini.go()}. {lamborgini.show_speed()}')
print(f'{lada.name} имеет цвет {lada.color}')
print(f'{lamborgini.name} - полицейский автомобиль? {lamborgini.is_police}')
print(f'{lada.name} - полицейский автомобиль? {lada.is_police}')
print(ferrari.show_speed())
print(kia.show_speed())
print(lamborgini.show_speed())
print(lada.show_speed())