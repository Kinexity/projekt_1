import math as m
import time

sqrt_list = []
length_of_sqrt_list = 0

def gen_and_check(sequence_sqrt_sum, sequence_length, possible_sequence_permutations, sqrt_list_index):
	possible_sequences_permutations_sum_local = 0
	places_to_insert_new_sqrt = sequence_length + 1
	for sqrt_to_insert_index in range(sqrt_list_index, length_of_sqrt_list):
		sqrt_to_insert = sqrt_list[sqrt_to_insert_index]
		max_possible_sqrts_inserted = m.floor(sequence_sqrt_sum / sqrt_to_insert)
		for number_of_sqrts_inserted in range(1, max_possible_sqrts_inserted + 1):
			possible_ways_to_insert = m.comb(number_of_sqrts_inserted + places_to_insert_new_sqrt - 1, number_of_sqrts_inserted)
			inserted_elements_sign_variations = 2 ** number_of_sqrts_inserted
			possible_sequence_permutations_local = possible_sequence_permutations * possible_ways_to_insert * inserted_elements_sign_variations
			new_sequence_sqrt_sum = sequence_sqrt_sum - number_of_sqrts_inserted * sqrt_to_insert
			new_sqrt_list_index = sqrt_to_insert_index + 1
			possible_sequences_permutations_sum_local += possible_sequence_permutations_local
			if (new_sqrt_list_index < length_of_sqrt_list):
				new_sequence_length = sequence_length + number_of_sqrts_inserted
				possible_sequences_permutations_sum_local += gen_and_check(new_sequence_sqrt_sum, new_sequence_length, possible_sequence_permutations_local, new_sqrt_list_index)
	return possible_sequences_permutations_sum_local

def run(a):
	global sqrt_list
	global length_of_sqrt_list
	n = int(m.ceil(m.sqrt(1 + 4 * a ** 2) + 1))
	sqrt_list = [m.sqrt(i / 2. * (i / 2. + 1)) for i in range(1,n)]
	length_of_sqrt_list = len(sqrt_list)
	return gen_and_check(a, 0, 1, 0)

for i in range(1, 200):
	start = time.perf_counter()
	res = run(i)
	koniec = time.perf_counter()
	print(i,"	", res, "	", round(koniec - start,5))
