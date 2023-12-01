import time


class TimerError(Exception):  # 5
    """Пользовательское исключение, используемое для сообщения об ошибках при использовании класса Timer"""


class Timer:

    def __init__(self):
        self._start_time = None

    def start(self):
        """Запуск нового таймера"""

        if self._start_time is not None:
            raise TimerError(f"Таймер уже работает. Используйте .stop() чтобы его остановить")

        self._start_time = time.perf_counter()

    def stop(self):
        """Отстановить таймер и сообщить о времени вычисления"""

        if self._start_time is None:
            raise TimerError(f"Таймер не работает. Используйте .start() для его запуска")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Вычисление заняло {elapsed_time:0.4f} секунд")


def divide(a, b):
    '''Обработка ошибок при делении на ноль'''
    try:
        result = int(a / b)
    except ZeroDivisionError:
        print("Попытка деления на ноль.")
        return float("inf")
    # except Exception:
    #     print("Перехвачена неожиданная ошибка!! ")
    except Exception as e:
        print(e)
    else:
        print("Деление произошло успешно.")
        return result


print(divide(25, 5.4))


# -----------------------------------------


def izm_time(func):
    ''' декоратор определяет время выполнения функции в секундах. '''

    def time2(*args, **kwargs):
        # print(args)
        # print(kwargs)
        tic = time.perf_counter()
        a = func(*args, **kwargs)
        toc = time.perf_counter()
        print(f"Вычисление заняло {toc - tic:0.6f} секунд")
        return a

    return time2


class TimerError(Exception):  # 5
    """Пользовательское исключение, используемое для сообщения об ошибках при использовании класса Timer"""


@izm_time
def test(n, d_calc):
    if n in d_calc:
        sum=d_calc[n]
    else:
        sum = 0
        for i in range(n):
            sum = sum + i
        d_calc[n]=sum
    return sum

d_calc = dict()
print(test(1000000, d_calc))

# -----------------------------------------
# 1/0
mytimer = Timer()
mytimer.start()
# mytimer.start()
print(test(1000000, d_calc))
mytimer.stop()
print('---4---')
start = time.time()
print(test(1000000, d_calc))
end = time.time()
print(f"Вычисление заняло {end-start:0.4f} секунд")
