import numpy as np
import itertools as it
import math as m
import time
import operator

start = time.clock()
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact
#funkcja silnia
list1=[]
list2=[]
sum=3
print(sum)
#suma maksymalna cyfr

x=1
while m.sqrt((x/2)*(x/2+1))<sum:
    x=x+1
c=x/2

lista={}
for q in range(1,int(2*c)):
	lista[q]=[]
lista[1]=[]
#zrobilem słownik list tak żeby było nie za dużo nie za mało
for x in range(1,int(2*c)):
	list1.append([m.sqrt((x/2)*(x/2+1)),str(x-1)])
for x in range(1,int(2*c)):
    list2.append([m.sqrt((x/2)*(x/2+1)),str(x-1+len(list1))])
	#list.append([x/2,str(x-1)])
	#list.append(-x/2)
#zrobiłem listę podlist długości 2: pierwsza cyfra podlisty- wartość funkcji m.sqrt((x/2)*(x/2+1))
#od liczby w podanym zbiorze, druga-indeks tej podlisty
lista[1]=sorted(list1+list2,key=lambda x:x[0])
#sortowanie wzgl. pierwszego elementu podlisty
index=0
#indeks list a>1
bindex=0
#indeks listy jedynkowej
count=len(lista[1])
#szukana liczba ciągów
list_number=1
#numer listy
try:
    while index<len(lista[list_number]):
        if lista[list_number][index][0]+lista[1][bindex][0] <sum:
            if str(lista[list_number][index][1]).find(str(bindex))==-1:
                lista[list_number+1].append([lista[list_number][index][0]+lista[1][bindex][0],str(lista[list_number][index][1])+str(bindex)])
            else:
                lista[list_number+1].append([lista[list_number][index][0]+lista[1][bindex][0],lista[list_number][index][1]])
            powtorzenia=list_number+1-len(str(lista[list_number+1][-1][1]))+1
            count=count+factorial(list_number+1-powtorzenia)*factorial(list_number+1)/(factorial(list_number+1-powtorzenia)*factorial(powtorzenia))
            index=index+1
#wpierw przelatuje indexy dla ustalonego bindexu i sprawdzam dla każdych dwóch ich sume. Jeśli indeks cyfry z listy początkowej(jedynek) nie wystąpił w drugiej cyfrze
#podlisty listy sum, to nie dolepiam tego indeksu do zlepku indeksów (drugiej cyfry podlisty), jak nie wystąpił to dolepiam ją do tego zlepka
#od drugiej linijki z kombinatoryki licze kombinacje dla ewentualnie tych samych bindexów w zlepku i nie tych samych (stosuje dwumian Newtona)
        if lista[list_number][index][0]+lista[1][bindex][0]>=sum:
            bindex=bindex+1
            index=0
#jak przeleciałem wszystkie indexy, przelatuje znowu te indexy tylko dla bindexu+1. Tu da się coś zoptymalizować.
        if bindex==len(lista[1])-1 and list_number<2*sum:
            list_number=list_number+1
            lista[list_number]=sorted(lista[list_number],key=lambda x:x[0])
            bindex=0
            index=0
            if list_number!=2:
                lista[list_number-1].clear()
#tutaj biorę krańcowy bindex. Po przeleceniu przez wszystkie indexy liczymy potem sumy dłuższych o 1 ciągów.
except KeyError:
	pass

try:
	print(count)
	'''print(lista[1])
	print(lista[2])
	print(lista[3])
	print(lista[4])
	print(lista[5])'''
#sprawdzenie, tylko po wykasowaniu ostatniego ifa!

except KeyError:
	pass
koniec=time.clock()
print(koniec-start)
