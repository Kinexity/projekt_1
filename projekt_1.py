import numpy as np

def test_condition(sequence, a):
	return np.sum(sequence) < a

def generate_sqrt_list(a):
	sqrt_list = []
	n = int(np.ceil(np.sqrt(1 + 4 * a ** 2) + 1))
	for i in range(1,n):
		sqrt_list.append(np.sqrt(n/2.*(n/2.+1)))
	return sqrt_list