print('Vvedite chislo')

def dividers(n): print(*[i for i in range(1, n + 1) if n % i == 0])

dividers(int(input()))
