# Melhor caso => O(n); Pior caso => O(n^2)
def bubble_sort(vet: list[int]):
	change = True
	len_vet = len(vet)
	while change:
		change = False
		len_vet -= 1
		for i in range(len_vet):
			if vet[i] > vet[i + 1]:
				vet[i], vet[i + 1] = vet[i + 1], vet[i]
				change = True


# Melhor, médio e pior caso => O(n^2)
def selection_sort(vet: list[int]):
	len_vet = len(vet)
	for i in range(len_vet):
		pos_less = i
		for j in range(i + 1, len_vet):
			if vet[j] < vet[pos_less]:
				pos_less = j
		vet[pos_less], vet[i] = vet[i], vet[pos_less]


def insertion_sort(vet: list[int]):
	for i in range(1, len(vet)):
		aux = vet[i]
		j = i - 1
		while (aux < vet[j]) and (j >= 0):
			vet[j + 1] = vet[j]
			j -= 1
		vet[j + 1] = aux


def quick_sort(vet: list[int]):
	if len(vet) <= 1:
		return vet
	pivot = vet[0]
	equal = [x for x in vet if x == pivot]
	less = [x for x in vet if x < pivot]
	more = [x for x in vet if x > pivot]

	return quick_sort(less) + equal + quick_sort(more)


def quick_sort2(vet: list[int], imin: int = 0, imax: int = None):
	if imax is None:
		imax = len(vet) - 1

	if imin < imax:
		pivot = vet[imin]
		i, j = imin + 1, imax
		while i <= j:
			while i <= j and vet[i] < pivot:
				i += 1
			while i <= j and vet[j] > pivot:
				j -= 1
			if i < j and vet[i] > vet[j]:
				vet[i], vet[j] = vet[j], vet[i]
		vet[imin], vet[j] = vet[j], pivot
		quick_sort2(vet, imin, j - 1)
		quick_sort2(vet, j + 1, imax)


def merge_sort(vet: list[int]):
	if len(vet) < 2:
		return
	mid = len(vet) // 2
	left = vet[:mid]
	right = vet[mid:]
	merge_sort(left)
	merge_sort(right)

	i = j = k = 0
	while (i < len(left)) and (j < len(right)):
		if left[i] < right[j]:
			vet[k] = left[i]
			i += 1
		else:
			vet[k] = right[j]
			j += 1
		k += 1

	while i < len(left):
		vet[k] = left[i]
		i, k = i + 1, k + 1

	while j < len(right):
		vet[k] = right[j]
		j, k = j + 1, k + 1
