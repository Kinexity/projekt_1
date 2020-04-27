import numpy as np
import itertools as it

def test_condition(sequence, sqrt_list, a):
	return np.sum(np.multiply(sequence,sqrt_list)) < a

def generate_sqrt_list(n):
	sqrt_list = []
	for i in range(1,n):
		sqrt_list.append(np.sqrt(i / 2. * (i / 2. + 1)))
	return np.array(sqrt_list)

def generate_sequences(n):
	return it.product(range(3), repeat=n-1)

def run(a):
	d_trn = [1,2,1]
	n = int(np.ceil(np.sqrt(1 + 4 * a ** 2) + 1))
	sqrt_list = generate_sqrt_list(n)
	sequences = [np.array(lst) for lst in generate_sequences(n)]
	correct_sequences = [sq for sq in sequences if test_condition(sq, sqrt_list, a)]
	transformed_sequences = [np.array([d_trn[elem] for elem in sq]) for sq in correct_sequences]
	sum = -1
	for sq in transformed_sequences:
		sum += np.prod(sq)
	return sum

for i in range(1, 11):
	print(i,"	",run(i))