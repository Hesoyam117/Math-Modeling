import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from settings import *

file = open("file.txt", "r")
#list1 = np.loadtxt("file.txt", delimiter='\t', dtype=np.float)
list1 = file.readline()
list2 = [0] * len(list1)
for i in range (0, len(list1)):
    list2[i] = float(list1[i] ** 2)

#func = pd.DataFrame({'x': list1, 'y': list2})
#plt.plot(func['x'], func['y'])
plt.scatter(list1, list2)
plt.show()
