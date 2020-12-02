class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def m_road(self):
        return f'{(self._length * self._width * 25 * 5) / 1000} тонн'


road = Road(5000, 20)
print(road.m_road())

