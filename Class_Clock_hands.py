# Создать имитатор часов, который при задании часов и минут возвращает угол поворота часовой и минутной стрелки.
# Вывести все возможные комбинации поворота стрелок, когда угол между ними равен 120°
# Написать класс и функцию для решения этой задачи
# Сравнить время выполнения (класс работает дольше на 10%)

import time


class Clock_hands:
    '''Класс для определения углового положения стрелок чесов и сопутствующих вычислений
    в зависимости от заданного времени'''

    def __init__(self, hour: int, minute: float):

        if hour > 11 or minute > 59.99:
            error_message = (f"Значение hour({hour}) или minute({minute}) "
                             f"вышли за диапазон (hour до 11, minute до 59.99)")
            print(error_message)
            self.hour = 0
            self.minute = 0

            # raise Exception(error_message)

        else:
            self.hour = hour
            self.minute = minute

    def update_hm(self, hour_new: int, minute_new: float):
        '''Изменение параметров час и минута с проверкой значений, для экземпляра Clock_hands '''
        if (hour_new > 11) or (minute_new > 59.99):
            self.hour = 0
            self.minute = 0.0
        else:
            self.hour = hour_new
            self.minute = minute_new

    def angles_calculation(self):
        '''Вычисляет угол поворота каждой стрелки на часах и угол между стрелками'''
        h_grad_hour = 30  # количество градусов для поворота часовой стрелки за 1 час
        h_grad_min = 0.1  # количество градусов для поворота часовой стрелки за 1 минуту
        m_grad_min = 6  # количество градусов для поворота минутной стрелки за 1 минуту
        angles = {'hour': self.hour, 'minute': self.minute, 'angles_hour_hands': 0, 'angles_minute_hands': 0,
                  'angles_between_clock_hands': 0.00}
        if self.hour > 11 or self.minute > 59.99:
            print(
                f"angles_calculation : Значение hour({self.hour}) или minute({self.minute})"
                f" вышли за диапазон (hour до 11, minute до 59.99)")
            return angles

        angles['angles_hour_hands'] = self.hour * h_grad_hour + self.minute * h_grad_min
        angles['angles_minute_hands'] = self.minute * m_grad_min
        angles_between_clock_hands = round(abs(angles['angles_hour_hands'] - angles['angles_minute_hands']),
                                           2)  # вычисляем угол между стрелками
        if angles_between_clock_hands > 180:  # если угол больше 180, то уменьшаем его вычитая из 360
            angles_between_clock_hands = round(360 - angles_between_clock_hands, 2)
        angles['angles_between_clock_hands'] = angles_between_clock_hands
        return angles


def d_cloc(h, m):
    cloc = {'h': h, 'm': m, 'hº': 0, 'mº': 0, 'uº': 0.00}
    if h > 11 or m > 59.99:
        print('Значение h или m вышли за диапазон (h до 11, m до 59.99)')
        return cloc

    h_grad_hour = 30  # количество градусов для поворота часовой стрелки за 1 час
    h_grad_min = 0.1  # количество градусов для поворота часовой стрелки за 1 минуту
    m_grad_min = 6  # количество градусов для поворота минутной стрелки за 1 минуту

    cloc['hº'] = h * h_grad_hour + h_grad_min * m
    cloc['mº'] = m * m_grad_min
    up = round(abs(cloc['hº'] - cloc['mº']), 2)  # вычисляем угол между стрелками
    if up > 180:  # если угол больше 180, то уменьшаем его вычитая из 360
        up = round(360 - up, 2)
    cloc['uº'] = up
    return cloc


start_time = time.perf_counter()
cl = d_cloc(40, 0)
print(cl)

i_max = 1000
j = 0
for i in range(i_max):
    for ih in range(12):
        for im in range(240):
            cm = im / 4
            cl = d_cloc(ih, cm)
            # print(ih, cm, cl)
            if abs(cl['uº'] - 120) < 0.6:
                j = j + 1
                # print(j, ih, cm, cl)

elapsed_time = time.perf_counter() - start_time
print(f"Вычисление заняло {elapsed_time:0.4f} секунд")

# cl = Clock_hands(4, 0)
# c = cl.angles_calculation()
# print(c)

start_time = time.perf_counter()
cl = Clock_hands(4, 60)
print('cl.hour = ', cl.hour, ' cl.minute = ', cl.minute)


for i in range(i_max):
    j = 0
    for ih in range(0, 12):  # часы
        for im in range(0, 240):  # минуты с долями до 0,25
            cm = im / 4
            cl.update_hm(ih, cm)
            cla = cl.angles_calculation()
            # print(ih, cm, cl)
            if abs(cla['angles_between_clock_hands'] - 120) < 0.6:  # выводит только для углов между стрелками = 120º
                j = j + 1
                if i == i_max-1:
                    print(j, ih, cm, cla)

elapsed_time = time.perf_counter() - start_time
print(f"Вычисление заняло {elapsed_time:0.4f} секунд")
