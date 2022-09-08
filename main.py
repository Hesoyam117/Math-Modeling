import matplotlib.pyplot as plt
import openpyxl as xl
book = xl.open("data.xlsx")
sheet = book.active
color = ["red", "green", "blue", "purple", "gray", "black"]
list1, list2 = [], []
run = True
while run == True:
    print('Инструкции по вводу данных в таблицу.\n В 1-й строке указываются значения X, \n в следующей строке указываются значения Y')
    print('Далее для ввода следущих наборов данных необходимо по аналогии вводить в нечетную строку X, а в чётную Y ')
    print('Укажите номера графиков для вывода через пробел:')
    choice = input()
    choice = list(map(int, choice.split(" ")))
    for i in range (0, sheet.max_column):
        for j in range(len(choice)):
            mlier = 2 * choice[j] - 1
            if sheet[mlier][i].value != None:
                list1.append(sheet[mlier][i].value)
                list2.append(sheet[mlier + 1][i].value)
            plt.scatter(list1, list2, c=color[j])
            list1, list2 = [], []
    plt.show()
    print('Для завершения работы нажмите 0')
    choice = input()
    if choice == "0":
        run = False
