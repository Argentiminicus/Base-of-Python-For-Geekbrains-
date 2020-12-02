class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Машина {self.name} - {self.color} цвет')

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {"направо" if direction == 1 else "налево"}')

    def show_speed(self):
        return f'Скорость {self.speed}'


class TownCar(Car):
    def show_speed(self):
        return f'Скорость {self.speed}, превышение!' if self.speed > 60 else f'Скорость {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'{self.name} - Скорость {self.speed}, превышение!' if self.speed > 40 else f'Скорость {self.speed}')


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


town = TownCar('Ока', 'белый', 70)
town.go()
print(town.show_speed())
town.turn(1)
town.stop()
print()

sport = SportCar('Ягуар', 'красный', 180)
sport.go()
print(sport.show_speed())
sport.turn(0)
sport.stop()
print()

work = WorkCar('Камаз', 'оранжевый', 40)
work.go()
print(work.show_speed())
work.turn(0)
work.stop()
print()

police = PoliceCar('Мент', 'бело-черный', 60)
police.go()
print(police.show_speed())
police.turn(0)
police.stop()
