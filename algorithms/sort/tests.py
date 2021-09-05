from sort import *
from random import sample, randint
from timeit import timeit


def generate_random_list(k: int) -> list[int]:
	return sample(range(0, k), k=k)


# encontra o tempo de execução de uma ordenação
def time_test(algname: str, vet: list[int], vet_sorted: list[int]):
	print('***************************************************')
	print(algname.upper())
	print(vet)
	print(vet_sorted)
	time = timeit(stmt=f'{algname}({vet})', setup=f'from __main__ import {algname}', number=1000)
	print(time)


# Compara a ordenação de várias listas com o mesmo tamanho e os mesmos numeros, mas embaralhadas de forma diferente
def comp_test(sort_func_name: str, list_len: int = 50, qtd_loops: int = 50):
	print(f'\033[1;{randint(31,36)}myou want to make a comparison test with {sort_func_name}? [Y/n]')
	if input('--> ').lower() != 'n':
		previous = []
		loop = 0
		comp = True
		while comp and loop < qtd_loops:
			print(f'({loop})')
			tosort = generate_random_list(list_len)
			print(tosort)
			eval(f'{sort_func_name}({tosort})')
			print(tosort)
			print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
			if len(previous) > 0:
				comp = tosort == previous
				previous = tosort
			loop += 1
		print(f'{sort_func_name} OK --> {comp}')


if __name__ == '__main__':

	def time_test_n01():
		nums = generate_random_list(100)

		tosort = nums.copy()
		bubble_sort(tosort)
		time_test('bubble_sort', nums.copy(), tosort)

		tosort = nums.copy()
		selection_sort(tosort)
		time_test('selection_sort', nums.copy(), tosort)

		tosort = nums.copy()
		insertion_sort(tosort)
		time_test('insertion_sort', nums.copy(), tosort)

		tosort = nums.copy()
		merge_sort(tosort)
		time_test('merge_sort', nums.copy(), tosort)

		tosort = nums.copy()
		tosort = quick_sort(tosort)
		time_test('quick_sort', nums.copy(), tosort)

		tosort = nums.copy()
		quick_sort2(tosort)
		time_test('quick_sort2', nums.copy(), tosort)


	def comp_test_n01():
		comp_test('bubble_sort')
		comp_test('selection_sort')
		comp_test('insertion_sort')
		comp_test('merge_sort')
		comp_test('quick_sort')
		comp_test('quick_sort2')


	time_test_n01()
	comp_test_n01()
