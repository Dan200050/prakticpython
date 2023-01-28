arr = []

arr_2 = []

for _ in range(10):

   arr.append(int(input('Введите число: ')))

for el in arr:

   if el not in arr_2:

       arr_2.append(el)

print(arr_2)
