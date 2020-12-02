from time import sleep


class TrafficLight:
    __color = 'Grey'

    def running(self):
        while True:
            print('Красный')
            sleep(7)
            print('Желтый')
            sleep(2)
            print('Зеленый')
            sleep(9)
            print('Желтый')
            sleep(2)


turning = TrafficLight()
turning.running()
