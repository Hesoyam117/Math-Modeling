import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from settings import *

file = open("file.txt", "r")
listmain = np.loadtxt("file.txt", delimiter='\t', dtype=np.float)
num = len(listmain) // 10
print('Найдено ', num, ' наборов данных, выберите сколько отобразить:\n 1-3: отобразить один из графиков')
choice = int(input())
if choice == 1:
    list1 = listmain[:10]
    list2 = list1[5:10]
    list1 = list1[:5]
    print(list1)
    print(list2)
elif choice == 2:
    list1 = listmain[10:20]
    list2 = list1[5:10]
    list1 = list1[:5]
    print(list1)
    print(list2)
elif choice == 3:
    list1 = listmain[20:30]
    list2 = list1[5:10]
    list1 = list1[:5]
    print(list1)
    print(list2)
else:
    print('Ошибка')


#list2 = [0] * len(list1)
#for i in range (0, len(list1)):
    #list2[i] = np.cos(list1[i])

#func = pd.DataFrame({'x': list1, 'y': list2})
#plt.plot(func['x'], func['y'])
plt.scatter(list1, list2)
plt.show()
