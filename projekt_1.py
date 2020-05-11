from __future__ import division
import itertools
import numpy as np
import math as m
import time
import operator
import array as arr

start = time.clock()
sumka=100
#suma maksymalna liczb

list=[]
lista=[]
x=1
while m.sqrt((x/2)*(x/2+1))<sumka:
    x=x+1
c=x/2
#tworzenie ograniczeń do listy pierwiastkow
for x in range(1,int(2*c)):
	list.append(m.sqrt((x/2)*(x/2+1)))
list.sort()
#tworzenie listy pierwiastkow
for m in range(0,int(2*c)-1):
    if list[m]<sumka:
        jedynka=m+1
    else:
        break
#szukanie ilości jedynek mniejszej od zadanej sumy, czyli indeks największego+1
def index_min_sum(leng,s=sumka):
    for index in range(0,len(list)-1):
        if leng*list[index]<sumka and leng*list[index+1]>sumka:
            return leng*index
#leng - dlugosc ciagu, szukamy sumy takich indeksów którym odpowiada najbliższa sumie-sumka wiartość

'''print("suma indeksów minimalna:",index_min_sum(leng))
print("suma indeksów maksymalna:",index_min_sum(leng)+leng)'''
#sprawdzenie

def sum_to_n(n, size, limit=None):
    """Produce all lists of `size` positive integers in decreasing order
    that add up to `n`."""
    if size == 1:
        yield [n]
        return
    if limit is None:
        limit = n
    start = (n + size - 1) // size
    stop = min(limit, n - size + 1) + 1
    for i in range(start, stop):
        for tail in sum_to_n(n - i, size - 1, i):
            yield [i] + tail
#funkcja nie bierze zer, trzeba ją zmodyfikować albo brać te indeksy i pomniejszyć wszystkie o 1
#wtedy suma indeksów z kombinacji w ciągu długosci leng bedzie mniejsza o leng

'''for partition in sum_to_n(sumka, leng):
    print (partition)'''
#sprawdzenie i bazgroly
lista=[]
szukana=0
#indeks przy którym jestesmy najbliżej sumki przy pozostalych indeksach takich samych
leng=2
while leng <=int(2*c):
    b=0
    i=int(index_min_sum(leng)/leng)
    while i<=int(index_min_sum(leng)+leng):
        if list[int(index_min_sum(leng)/leng)]*(leng-1)+list[i]<sumka:
            szukana=i
            i+=1
        else:
            break
    '''print(szukana)'''
    '''print(list)'''
#szukam jak u cb zwiększając jeden indeks z indeksów takich samych aż osiągnie sumke

    suma_indeksów=(index_min_sum(leng)/leng)*(leng-1)+szukana
    #suma indeksow jak u cb
    liczba=0
    for partition_0 in sum_to_n(int(suma_indeksów)+int(leng), int(leng)):
#tu uwzględniam to co wspominalem ze liczac od 0 trzeba zwiekszyc sume o leng
        print (partition_0)
        sum=0
        for index in range(0,leng):
            sum=sum+list[partition_0[index]-1]
        lista.append(sum)
        for liczba1 in lista:
            if liczba1>=sumka:
                lista.remove(liczba1)

#lista sum
    '''for liczba1 in lista:
        if liczba1>=sumka:
            lista.remove(liczba1)'''

#usuwam te kombinacje  większe od sumki
    a=max(lista)
#licze maksymalna dla listy żeby potem wyznaczyc sume graniczną indeksow
    for partition_1 in sum_to_n(int(suma_indeksów+1)+int(leng), int(leng)):
#tu uwzględniam to co wspominalem ze liczac od 0 trzeba zwiekszyc sume o leng
        print (partition_1)
        sum=0
        for index in range(0,leng):
            sum=sum+list[partition_1[index]-1]
        lista.append(sum)
        for liczba2 in lista:
            if liczba2>=sumka:
                lista.remove(liczba2)
#lista sum
    '''print(lista)'''
#tak jak wczesniej usuwam wszystkie wieksze od sumki
    if max(lista)>a:
        b=1
#porownuje jak zwiekszyla sie dlugosc listy względem poprzedniego a, to część z kombinacji indeksow
#dajacych sume suma_indeksów+1 jest mniejsza od sumki, czyli jest własniwym indeksem granicznym
#zamiast suma_indeksów
    '''b=b+len(lista)*(2**(leng-1))'''
#na początku wzialem b=0. licze wklady do sum od wszystkich dlugosci ciagow o sumach indeksow
#granicznych. 2**(leng-1) wynika z kombinatoryki

    print(suma_indeksów+b)
    #szukany indeks graniczny
    '''print(lista)'''
    print(max(lista))
    #maksymalna suma mniejsza od a
    lista.clear()
#czyszcze po kazdej dlugosci ciagu'''
    leng+=1
    '''print(b)'''

#-----------------------------------------------------------------------------------------------------------------------------------------
#dalej trzeba policzyc manualnie kombinacje indeksow o sumach mniejszych (banalne) tylko trzeba uwzglednic ujemne liczby.
koniec=time.clock()
print(koniec-start)
