from random import *
from random import randint 
from random import sample

bublemass = sample(range(20),20) # return list of k random elements from population
print(bublemass)
count = 0
for j in range(len(bublemass) - 1):
	for i in range(0, len(bublemass) - 1 - j):
		if bublemass[i] > bublemass[i+1]:
			count += 1
			bublemass[i],bublemass[i+1] = bublemass[i+1],bublemass[i]
print(bublemass)
print(count)#кол-во итеарций


#0----2

print("2 exersice")
arr = [] 
r  = 20
c = 5
for i in range(r):
	for j in range(c):
		secArr = sample(range(1,100),5) #random unique number from 1,100
	arr.append(secArr)

for i in arr:
	for j in  i:
		print (j, end = " ")
	print()

for i in range(len(arr)):
	if min(arr[i]) % 2 == 0:
		arr[i][arr[i].index(min(arr[i]))] = 0
	else:
		arr[i][arr[i].index(min(arr[i]))] = 1

print( )

for i in arr:
	for j in  i:
		print (j, end = " ")
	print()
