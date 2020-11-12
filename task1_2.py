while True:
    sec = int(input('Введи время в секундах целым положительным числом: '))
    if sec <= 0:
        continue
    else:
        hours = sec // 3600
        minutes = (sec % 3600) // 60
        seconds = (sec % 3600) % 60
        print(f'Ваше время в формате чч.мм.сс: {hours:02}.{minutes:02}.{seconds:02}')
        break
