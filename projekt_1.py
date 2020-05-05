import numpy as np
import itertools as it
import math as m
import time

fact = [m.factorial(i) for i in range(1000)]
a = 0
sqrt_list = []
ln_sqrt_list = 0

def gen_and_check(sum, length, multiplier, sqrt_list_index):
	posibilities = 0
	if (sum < a):
		if (length > 0):
			posibilities += fact[length] * multiplier
		if (sqrt_list_index < ln_sqrt_list):
			elem = sqrt_list[sqrt_list_index]
			for sqrt_list_index_it in range(sqrt_list_index + 1, ln_sqrt_list):
				posibilities += gen_and_check(sum + elem, length + 1, multiplier * 2, sqrt_list_index_it)
				posibilities += gen_and_check(sum + 2 * elem, length + 2, multiplier, sqrt_list_index_it)
	return posibilities


def run(a_arg):
	global sqrt_list
	global a
	global ln_sqrt_list
	a = a_arg
	n = int(np.ceil(np.sqrt(1 + 4 * a ** 2) + 1))
	sqrt_list = [np.sqrt(i / 2. * (i / 2. + 1)) for i in range(1,n)]
	ln_sqrt_list = len(sqrt_list)
	return gen_and_check(0, 0, 1, 0)

for i in range(2, 200):
	start = time.perf_counter()
	res = run(i)
	koniec = time.perf_counter()
	print(i,"	", res)
	print(koniec - start)
