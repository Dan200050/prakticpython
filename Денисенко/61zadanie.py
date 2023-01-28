arr = []

for _ in range(10):

   arr.append(int(input('Введите число: ')))

for i in range(9):

   if arr[i] < 0 and arr[i + 1] < 0:

       print('Пара:', arr[i], arr[i + 1])

print()
