import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from settings import *
file = open("file.txt", "r")
listmain = np.loadtxt("file.txt", delimiter='\t', dtype=np.float)
num = len(listmain) // 10
print('Правила ввода данных в файл:\n Первые 10 строчек - ось x, следующие 10 - ось y.\n Далее по аналогии. Можно ввести от 1-го до 3-х графиков')
print('Найдено ', num, ' наборов данных, выберите сколько отобразить:\n 1-3: отобразить один из графиков\n 4: отобразить все графики')
choice = int(input())
list12 = []
list13 = []
list22 = []
list23 = []
if choice == 1:
    list1 = listmain[:20]
    list2 = list1[10:20]
    list1 = list1[:10]
    print(list1)
    print(list2)
elif choice == 2:
    list1 = listmain[20:40]
    list2 = list1[10:20]
    list1 = list1[:10]
    print(list1)
    print(list2)
elif choice == 3:
    list1 = listmain[40:360]
    list2 = list1[10:20]
    list1 = list1[:10]
    print(list1)
    print(list2)
elif choice == 4:
    list1 = listmain[:10]
    list12 = listmain[20:30]
    list13 = listmain[40:50]
    list2 = listmain[10:20]
    list22 = listmain[30:40]
    list23 = listmain[50:60]
else:
    print('Ошибка')
plt.scatter(list1, list2)
plt.scatter(list12, list22)
plt.scatter(list13, list23)
plt.show()
