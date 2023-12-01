# Поворот квадратного списка на 90 г по часовой стрелке
import numpy as np
import datetime
import time

def printm(m:tuple,mname : str):
  """ Распечатывает матрицу """
  print(f'-----{mname}-----')
  for x in m:
    print(x)

def create_matrix(nlen:int,istart:int= 1, step:int = 1):
  n=nlen
  matrix_out = [[istart+i*step + n*j*step for i in range(n)] for j in range(n)]
  return matrix_out

def create_matrix_n(nlen:int, val:int):
  n=nlen
  matrix_out = [[val for i in range(n)] for j in range(n)]
  return matrix_out

nm=6000
print('Размер таблицы :', nm)
d=create_matrix(nm)
# printm(d,'исходный список')
# d.reverse()
# printm(d,'d1')
# e2 = zip(*d[::-1])
f=d[::-1]
# printm(f,'поменян порядок, до разворота')
print(id(d))
tic = time.perf_counter()
t=tuple(zip(*d[::-1])) # t- промежуточный картеж для переноса трансформированных
                       # данных в исходный список d.
# for i in range(nm):
#   for j in range(nm):
#     d[i][j]=t[i][j]

toc = time.perf_counter()
print(f"Вычисление 1 заняло {toc - tic:0.6f} секунд")
print(id(d))
# printm (d,'d)')
# printm(e3,'Повернут с помощью zip(*d[::-1]')
# ниже используем функционал numpy
tic = time.perf_counter()
rotated_matrix = np.rot90 (d, k=-1)
# for i in range(nm):
#   for j in range(nm):
#     d[i][j] = rotated_matrix[i][j]
toc = time.perf_counter()
print(f"Вычисление 2 заняло {toc - tic:0.6f} секунд")
# print (rotated_matrix)
# printm (rotated_matrix,'np.rot90 (d, k=-1)')

tic = time.perf_counter()
n = nm - 1
x = 0
for i in range((nm) // 2):
    # print('+++++++++++++++++++++ i=', i)
    for j in range((nm + 1) // 2):
        # print('==================== j=', j)
        x += 1
        delta = n - j
        # print('x, i, j, delta : ',x,':', i, j, '-', delta,i)
        tmp = d[i][j]  # куда
        # who=d[delta][i]
        # print('///что ///куда///',who, tmp )

        # print('from',d[delta][i],'to', d[i][j])
        # d[i][j]=d[delta][i]
        # print('+++++++++++++', tmp )
        i1 = i
        j1 = j
        delta1 = delta
        x1 = 0
        for k in range(3):
            x1 += 1
            # print('x1, i1, j1, delta : ',x1,':', i1, j1, '- ', delta1, i1)

            # to1  = d[i1][j1] # куда
            # who1 = d[delta1][i1] # что
            # print('/x1=',x1, '\\\что \\\куда\\\\',who1, to1 )
            # tmp=d[j1][delta]
            # print(d[delta1][i1], d[i1][j1])
            d[i1][j1] = d[delta1][i1]  # Присвоение значения ячейке назначения

            # Пересчет координат ячеек для перемещения значения
            j1 = i1
            i1 = delta1
            delta1 = n - j1

        # print('d,tmp',d[i1][j1], tmp)
        d[i1][j1] = tmp  # Присвоение запомненного значения после последней итерации
toc = time.perf_counter()
print(f"Вычисление 3 заняло {toc - tic:0.6f} секунд")
# printm(c,'c')
# printm(d,'d')