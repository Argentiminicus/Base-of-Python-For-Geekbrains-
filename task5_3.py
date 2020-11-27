with open('text_3.txt', 'r', encoding='utf-8') as file:
    empoloyes = {line.split()[0]: float(line.split()[1]) for line in file}
    print(
        f'Сотрудники с зарплатой меньше, чем 20000:'
        f' {[employee[0] for employee in empoloyes.items() if employee[1] < 20000]}\n'
        f'Средняя зарплата сотрудников {sum(empoloyes.values()) / len(empoloyes)}')
