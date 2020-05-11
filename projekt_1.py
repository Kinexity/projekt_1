#Autorzy: Szymon Augustynowicz, Jakub Żak
#Algorytm posiada złożoność wykładniczą o podstawie wynoszącej około 1,33.

import math as m
import time

#we wszystkich komentarzach słowo "pierwiastek" odnosi się do wyrazów sqrt(|m_i|(|m_i|+1))
sqrt_list = [] #lista pierwiastków

#count - rekurencyjna funkcja licząca ile jest ciągów o określonych parametrach
#sequence_sqrt_sum - zmienna opisująca, ile pierwiastków może zostać dołożonych
#sequence_length - aktualna długość ciągu
#possible_sequence_permutations - ilość permutacji danego ciągu
#sqrt_list_index - indeks następny w liście pierwiastków po indeksie ostatniego włożonym pierwiastka
#powyższe 4 parametry opisują ciąg badany na poprzednim etapie rekurencji
def count(sequence_sqrt_sum, sequence_length, possible_sequence_permutations, sqrt_list_index): 
	possible_sequences_permutations_sum_local = 0 #zmienna zliczająca ile ciągów o sumie pierwiastków mniejszej od a znaleziono na tym i niższych poziomach rekurencji
	places_to_insert_new_sqrt = sequence_length + 1 #liczba miejsc, gdzie można wstawić nowe wyrazy w ciągu włącznie z pozycjami na początku i na końcu
	for sqrt_to_insert_index in range(sqrt_list_index, len(sqrt_list)): #wybieranie następnego pierwiastka do dodania do sumy z listy pierwiastków
		sqrt_to_insert = sqrt_list[sqrt_to_insert_index] #branie pierwiastka z listy
		max_possible_sqrts_inserted = m.floor(sequence_sqrt_sum / sqrt_to_insert) #obliczanie ile razy można dodać pierwiastek do sumy pierwiestków, żeby ta dalej spełniała warunek mniejszości od a
		for number_of_sqrts_inserted in range(1, max_possible_sqrts_inserted + 1): #wybiarenie kolejnych ilości dodań pierwiastka do sumy
			#kombinatoryczne wyliczenie na ile sposobów można włożyć daną liczbę elementów (niezależnie od jego znaku) odpowiadajacych pierwiastkowi do ciągu
			#ze wzoru na liczbę kombinacji z powtórzeniami
			possible_ways_to_insert = m.comb(number_of_sqrts_inserted + places_to_insert_new_sqrt - 1, number_of_sqrts_inserted) 
			inserted_elements_sign_variations = 2 ** number_of_sqrts_inserted #na ile sposobów można dobrać znak do danej ilości elementów dodanych do ciągu
			possible_sequence_permutations_local = possible_sequence_permutations * possible_ways_to_insert * inserted_elements_sign_variations #ile permutacji posiada nowo powstały ciąg
			new_sequence_sqrt_sum = sequence_sqrt_sum - number_of_sqrts_inserted * sqrt_to_insert #ilość "miejsca" na dalsze pierwiastki w sumie pierwiastków nowego ciągu
			new_sqrt_list_index = sqrt_to_insert_index + 1 #kolejny indeks na liście pierwiastków
			possible_sequences_permutations_sum_local += possible_sequence_permutations_local #dodanie liczby możliwych permutacji tego ciągu do sumy permutacji na tym poziomie rekurencji
			if (new_sqrt_list_index < len(sqrt_list)): #sprawdzenie, czy indeks nie wyjechał poza zasięg
				new_sequence_length = sequence_length + number_of_sqrts_inserted #długość nowego ciągu
				#dodanie sumy liczby permutacji ciągów z niższych poziomów rekurencji do sumy na tym poziomie
				possible_sequences_permutations_sum_local += count(new_sequence_sqrt_sum, new_sequence_length, possible_sequence_permutations_local, new_sqrt_list_index) 
	return possible_sequences_permutations_sum_local #zwracanie sumy liczby permutacji ciągów z tego poziomu

#run - funkcja obliczająca wstępne dane do zliczania ciągów na podstawie danego a
def run(a):
	global sqrt_list
	n = int(m.ceil(m.sqrt(1 + 4 * a ** 2) + 1)) #długość listy pierwiastków wyznaczona z równania a = sqrt(n/2(n/2+1))
	sqrt_list = [m.sqrt(i / 2. * (i / 2. + 1)) for i in range(1,n)] #tworzenie listy pierwiastków, wyrazy o przeciwnych znakach dają takie same pierwiastki, więc liczymy je tylko od wyrazów dodatnich
	return count(a, 0, 1, 0)

for a in range(1, 200):
	start = time.perf_counter()
	res = run(a)
	koniec = time.perf_counter()
	print(a,"	", res, "	", round(koniec - start,5))
