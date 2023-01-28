import random
from random import *
from random import randint
from random import sample

with open("MusinVvod.txt", "w") as file:
    r = 0
    arr=[]
    try:
        r = int(input("введите размер массива(от 2 до 100): "))
        if 2>r>100:
            raise ValueError()
    except ValueError:
        print("не верная размерность массива, попробуй еще")

    arr = sample(range(1,200), r) #генерим случайные неповторяющиеся значения в массиве

    for i in range(len(arr)):
        file.write(str(arr[i]) + " ")
    print("файл MusinVvod.txt с массивом создан в папке с исходником проекта" + "\n")

arr= []

with open("MusinVvod.txt", "r+") as file:
    for line in file:
        for num in line.strip().split():#берем обрезанную строку и то что стоит между пробелами
            arr.append(int(num)) #записывает в массив то что стояло между пробелами
    print("original array in file: ", arr)
    count = 0
    for j in range(len(arr) - 1):
        for i in range(0, len(arr) - 1 - j):
            if arr[i] > arr[i + 1]:
                count += 1
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print("bouble sorted array: ",arr)
    print("iterations: ", count)  # кол-во итеарций

with open('Musinvivod.txt', 'w') as file:
    file.write("buble sorted mass: " + str(arr))  # записали массив в виде строки
    print("\n" + "массив успешно записан в файл Musinvivod.txt" + "\n")

print("--------------------------2th part----------------------------------------------------------------")
#Expected array generted by code below

with open("MusinVvod2.txt", "w") as file:#here we're generating array and write its in file
    print("файл MusinVvod2.txt с массивом создан в папке с исходником проекта"+"\n")
    arr= []
    r = 0
    c = 0

    try:
        r = int(input("Введите кол-во строк массива(от 1 до 100): "))
        c = int(input("Введите кол-во колонок массива(от 1 до 100): "))
        if 1 > r > 100:
            raise ValueError()
    except ValueError:
        print("Размерность массива введена неверно, попробуйте снова...")

    for i in range(r+1):
        secArr = sample(range(1, 200), c)  # random unique number from 1,100
        arr.append(secArr)
    for i in range(len(arr)-1):
        for j in range(c):
            file.write(str(arr[i][j])+" ")
        file.write("\n")

with open("Musinvvod2.txt", "r") as file:#тут мы выводим массив из файла в переменную lines
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip().split(' ')#каждую строку в лайнс обрезали по бокам от лишних символов(strip) и вставили числа которые находятся между пробелами(split)
        lines[i] = list(map(int, lines[i])) #сконевртировали каждый элемент строки из str в int
        print(lines[i])
#-----------------------handling with array------------------------------------
    for i in range(len(lines)):
        if min(lines[i]) % 2 == 0:
            lines[i][lines[i].index(min(lines[i]))] = 0 #если результат деления без остатка то замена на 0
        else:
            lines[i][lines[i].index(min(lines[i]))] = 1 #если результат деления с остатком то замена на 1
    print()
    for i in range(len(lines)):
        print(lines[i])

with open("Musinvivod2.txt", "w") as file:
    for i in range(len(lines)):
        for j in range(c):
            file.write(str(lines[i][j])+" ")
        file.write("\n")
    print("\n" + "массив успешно записан в файл Musinvivod2.txt")
