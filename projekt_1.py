import numpy as np
import itertools as it
import math as m
import time

factorials_list = [m.factorial(i) for i in range(1000)]
a = 0
sqrt_list = []
length_of_sqrt_list = 0

def gen_and_check(sequence_sqrt_sum, sequence_length, possible_sequence_permutations, sqrt_list_index):
	possible_sequences_permutations_sum_local = 0
	places_to_insert_new_sqrt = sequence_length + 1
	new_sum = a - sequence_sqrt_sum
	for sqrt_to_insert_index in range(sqrt_list_index, length_of_sqrt_list):
		sqrt_to_insert = sqrt_list[sqrt_to_insert_index]
		max_possible_sqrts_inserted = m.floor(new_sum / sqrt_to_insert)
		for number_of_sqrts_inserted in range(1, max_possible_sqrts_inserted + 1):
			possible_ways_to_insert = m.comb(number_of_sqrts_inserted + places_to_insert_new_sqrt - 1, number_of_sqrts_inserted)
			inserted_elements_sign_variations = 2 ** number_of_sqrts_inserted
			possible_sequence_permutations_local = possible_sequence_permutations * possible_ways_to_insert * inserted_elements_sign_variations
			new_sequence_sqrt_sum = sequence_sqrt_sum + number_of_sqrts_inserted * sqrt_to_insert
			new_sqrt_list_index = sqrt_to_insert_index + 1
			possible_sequences_permutations_sum_local += possible_sequence_permutations_local
			if (new_sqrt_list_index < length_of_sqrt_list):
				new_sequence_length = sequence_length + number_of_sqrts_inserted
				possible_sequences_permutations_sum_local += gen_and_check(new_sequence_sqrt_sum, new_sequence_length, possible_sequence_permutations_local, new_sqrt_list_index)
	return possible_sequences_permutations_sum_local

def gen_and_check_debug(sequence_sqrt_sum, sequence_length, possible_sequence_permutations, sqrt_list_index, check_list):
	possible_sequences_permutations_sum_local = 0
	places_to_insert_new_sqrt = sequence_length + 1
	new_sum = a - sequence_sqrt_sum
	for sqrt_to_insert_index in range(sqrt_list_index, length_of_sqrt_list):
		sqrt_to_insert = sqrt_list[sqrt_to_insert_index]
		max_possible_sqrts_inserted = m.floor(new_sum / sqrt_to_insert)
		for number_of_sqrts_inserted in range(1, max_possible_sqrts_inserted + 1):
			possible_ways_to_insert = m.comb(number_of_sqrts_inserted + places_to_insert_new_sqrt - 1, number_of_sqrts_inserted)
			inserted_elements_sign_variations = 2 ** number_of_sqrts_inserted
			possible_sequence_permutations_local = possible_sequence_permutations * possible_ways_to_insert * inserted_elements_sign_variations
			new_sequence_sqrt_sum = sequence_sqrt_sum + number_of_sqrts_inserted * sqrt_to_insert
			check_list_copy = list(check_list) # testing
			check_list_copy.append(number_of_sqrts_inserted) # testing
			print(check_list_copy, "	", possible_sequence_permutations_local, "		", new_sequence_sqrt_sum) # testing
			new_sqrt_list_index = sqrt_to_insert_index + 1
			possible_sequences_permutations_sum_local += possible_sequence_permutations_local
			if (new_sqrt_list_index < length_of_sqrt_list):
				new_sequence_length = sequence_length + number_of_sqrts_inserted
				possible_sequences_permutations_sum_local += gen_and_check_debug(new_sequence_sqrt_sum, new_sequence_length, possible_sequence_permutations_local, new_sqrt_list_index, check_list_copy)
		check_list.append(0) # testing
	return possible_sequences_permutations_sum_local

def new_run(a_arg):
	global sqrt_list
	global a
	global length_of_sqrt_list
	a = a_arg
	n = int(m.ceil(m.sqrt(1 + 4 * a ** 2) + 1))
	sqrt_list = [m.sqrt(i / 2. * (i / 2. + 1)) for i in range(1,n)]
	length_of_sqrt_list = len(sqrt_list)
	maximal_sequence_length = m.floor(a / sqrt_list[0])
	possible_sequences = 0
	for sequence_lenght in range(1, maximal_sequence_length + 1):
		#print("	sequence_lenght ",sequence_lenght)
		max_lower_sqrt_list_index = 0
		for sqrt_list_index in range(length_of_sqrt_list + 1):
			#print("sqrt_list_index ",sqrt_list_index)
			#print("sequence_lenght * sqrt_list[sqrt_list_index] ",sequence_lenght * sqrt_list[sqrt_list_index])
			if (sqrt_list_index == length_of_sqrt_list or sequence_lenght * sqrt_list[sqrt_list_index] > a):
				max_lower_sqrt_list_index = sqrt_list_index - 1
				break
		#print("max_lower_sqrt_list_index ",max_lower_sqrt_list_index)
		max_higher_sqrt_list_index_occurences = 0
		for higher_sqrt_list_index_occurences in range(sequence_lenght + 1):
			#print("higher_sqrt_list_index_occurences ",higher_sqrt_list_index_occurences)
			#print("thing ", higher_sqrt_list_index_occurences * sqrt_list[max_lower_sqrt_list_index + 1] + (sequence_lenght - higher_sqrt_list_index_occurences) * sqrt_list[max_lower_sqrt_list_index])
			if (higher_sqrt_list_index_occurences * sqrt_list[max_lower_sqrt_list_index + 1] + (sequence_lenght - higher_sqrt_list_index_occurences) * sqrt_list[max_lower_sqrt_list_index] > a):
				max_higher_sqrt_list_index_occurences = higher_sqrt_list_index_occurences - 1
				break
		#print("max_higher_sqrt_list_index_occurences ",max_higher_sqrt_list_index_occurences)
		max_index_sum = (sequence_lenght - max_higher_sqrt_list_index_occurences) * max_lower_sqrt_list_index + max_higher_sqrt_list_index_occurences * (max_lower_sqrt_list_index + 1)
		#print("max_index_sum ",max_index_sum)
		possible_sequences += sum([m.comb(index_sum + sequence_lenght - 1, index_sum) for index_sum in range(0, max_index_sum + 1)]) * 2 ** sequence_lenght
	return possible_sequences




def run(a_arg, debug):
	global sqrt_list
	global a
	global length_of_sqrt_list
	a = a_arg
	n = int(m.ceil(m.sqrt(1 + 4 * a ** 2) + 1))
	sqrt_list = [m.sqrt(i / 2. * (i / 2. + 1)) for i in range(1,n)]
	length_of_sqrt_list = len(sqrt_list)
	if (debug): # debug
		print(sqrt_list)
		return gen_and_check_debug(0, 0, 1, 0, [])
	else:
		return gen_and_check(0, 0, 1, 0)

db = False
for i in range(1, 200):
	print("Iteration: ", i)
	start = time.perf_counter()
	res = run(i, db)
	koniec = time.perf_counter()
	print(i,"	", res, "	", round(koniec - start,5))
	start = time.perf_counter()
	res = new_run(i)
	koniec = time.perf_counter()
	print(i,"	", res, "	", round(koniec - start,5))
	#if (db):
	input()
