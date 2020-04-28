import numpy as np
import itertools as it
import math as m
import time

start = time.clock()
#lista=[]
#lista2=[]
lista3 = []
lista4 = []
lista5 = []
for i in range(1,2 * 3):
	#lista.append(m.sqrt((i/2)*(i/2+1)))
	#lista2=lista+lista
	#lista2.sort()
	lista3.append(i / 2)
	lista4 = lista3 + lista3
	lista4.sort()
	#rozważamy same dodatnie
print(lista4)
count,start,a,b,end = 0,0,0,2,2
#print(suma)
try:
	while a <= 4 * (3 - 0.5) - 3:
		suma = sum(lista4[a:b])
		if lista4[end] + suma < 3:
			lista5.append(lista4[a])
			lista5.append(lista4[b - 1])
			lista5.append(lista4[end])
			print(lista5)
			lista5.clear()
			count+=1
			end+=1
			print(count)
		else:
			end = b + 1
			b+=1
			#print(b)
		if b > 4 * (3 - 0.5) - 1:
			a = a + 1
			b = a + 2
			end = b
		if end > 4 * (3 - 0.5) - 1:
			end = b + 1
			b+=1
			suma = suma - lista4[b - 2] + lista4[b - 1]
except IndexError:
	pass

koniec = time.clock()
print(koniec - start)
