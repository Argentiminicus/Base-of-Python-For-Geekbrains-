class Stationery:
    def __init__(self, title='Пейзаж'):
        self.title = title

    def draw(self):
        print(f'Отрисовка {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} нарисован ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} нарисован карандашом')


class Marker(Stationery):
    def draw(self):
        print(f'{self.title} нарисован маркером')


stuff = Stationery()
stuff.draw()

pen = Pen('Рисунок')
pen.draw()

pencil = Pencil('Чертеж')
pencil.draw()

marker = Marker('График')
marker.draw()


