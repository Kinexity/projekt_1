import numpy as np
import itertools as it
import math as m
import time

start = time.clock()
list=[]
s=16
c=m.ceil(2*s)/2

print(s)
#suma maksymalna cyfr

lista={}
for q in range(1,int(2*c)):
	lista[q]=[]
lista[1]=[]
for x in range(1,int(2*c)):
	#lista[1].append(m.sqrt((i/2)*(i/2+1)))
	list.append(x/2)
	list.sort()

lista[1]=list
i=0
#indeks listy jedynkowej
b=0
#indeks list a>1
count=0

c=1
#numer listy

try:
	while i<len(lista[c]):
		if lista[c][i]+lista[1][b]<s:
			lista[c+1].append(lista[c][i]+lista[1][b])
			'''lista[c+1].sort()'''
			i=i+1
		if lista[c][i]+lista[1][b]>=s and b<len(lista[1])-1:
			b=b+1
			i=0
		'''if lista[c][i]-lista[1][0]>=s:
			c=c+1
			b=0'''
		if b==len(lista[1])-1 and c<2*s:
			c=c+1
			b=0
			count=count+len(lista[c-1])
			if c!=2:
				lista[c-1].clear()
except KeyError:
	pass
print(count)
'''print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista[5])'''
#sprawdzenie

koniec=time.clock()
print(koniec-start)
